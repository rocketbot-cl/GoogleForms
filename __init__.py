# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import os
import json
import traceback

# import sys # it's already in rocketbot main

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"]  # type:ignore
google_directory_path = os.path.join(base_path, "modules", "GoogleForms")
gd_libs_path = os.path.join(google_directory_path, "libs")  # type:ignore

if gd_libs_path not in sys.path:  # type: ignore
    sys.path.append(gd_libs_path)  # type: ignore

"""
The code of each module works as a local scope. Each command that is executed resets the data.
To share information between commands, declare the variable as global. The sintax will be 'mod_modulename' or similar
"""
global mod_google_directory

"""
To connect to multiple databases, a dictionary is created and stores the instance of each connection.
The syntax is {"session name": {data}}
"""
SESSION_DEFAULT = "default"
try:
    if not mod_google_directory:  # type:ignore
        mod_google_directory = {SESSION_DEFAULT: {}}
except NameError:
    mod_google_directory = {SESSION_DEFAULT: {}}


class GoogleDirectory:
    """Google Authentication Class

    Raises:
        e: _description_
    """

    def __init__(self, credential_path) -> None:
        self.SCOPES = [
            "https://www.googleapis.com/auth/forms.body",
            "https://www.googleapis.com/auth/forms.responses.readonly",
        ]
        self.DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
        self.credential_path = credential_path
        self.form_service = None

    def config_credentials(self, output_path, port):
        """Configure the credentials."""
        from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore
        from googleapiclient import discovery  # type: ignore
        

        self.creds = None

        if not self.creds or self.creds.invalid:
            flow = InstalledAppFlow.from_client_secrets_file(
                self.credential_path, self.SCOPES
            )
            self.creds = flow.run_local_server(port=port)
            
            credentials_file = {"token": self.creds.token, "refresh_token": self.creds.refresh_token, "uri": self.creds.token_uri, "client_id": self.creds.client_id, "secret": self.creds.client_secret, "scopes": self.creds.scopes}
            
            with open(os.path.join(output_path, "credentials.json"), "w") as file:
                json.dump(credentials_file, file)
            
        self.form_service = discovery.build("forms", "v1", credentials=self.creds)
    
    def validate_credentials(self, file):
        from google.auth.transport.requests import Request # type: ignore
        from google.oauth2.credentials import Credentials # type: ignore
        from googleapiclient import discovery  # type: ignore
        
        with open(file, "r") as f:
            data = json.load(f)
        
            self.creds = Credentials(
                token=data['token'],
                refresh_token=data['refresh_token'],
                token_uri=data['uri'],
                client_id=data['client_id'],
                client_secret=data['secret'],
                scopes=data['scopes']
            )
            
            if self.creds.expired:
                self.creds.refresh(Request())
            
            self.form_service = discovery.build("forms", "v1", credentials=self.creds)
            
            credentials_file = {"token": self.creds.token, "refresh_token": self.creds.refresh_token, "uri": self.creds.token_uri, "client_id": self.creds.client_id, "secret": self.creds.client_secret}
        
        with open(file, "w") as f:
            json.dump(credentials_file, f)

try:
    # Get data from robot
    module = GetParams("module")  # type:ignore # Get command executed
    session = GetParams("session")  # type:ignore # Get Session name
    result = GetParams("result")  # type:ignore # Get variable name where save results

    if not session:
        session = SESSION_DEFAULT  # Set default session

    if module == "connect_forms":
        credentials_path = GetParams("credentials_path")  # type:ignore
        port = 8080 if not GetParams("port") else GetParams("port") # type:ignore

        google_directory = GoogleDirectory(credentials_path)

        try:
            creds_file = os.path.join(google_directory_path, "credentials.json")
            
            if os.path.exists(creds_file):
                google_directory.validate_credentials(creds_file)
            else:            
                google_directory.config_credentials(google_directory_path, port)
            
            mod_google_directory[session] = google_directory
            SetVar(result, True)  # type:ignore

        except Exception as e:
            SetVar(result, False)  # type:ignore
            traceback.print_exc()
            PrintException()  # type:ignore
            raise e

    if module == "create_form":
        # The field "input_" is left intentionally to catch up with the if cycle.
        # Just after the if is confirmed a function GetParams is called and stored in a meaningful variable
        # create_form_option = GetParams("option_")

        create_form_option = "create_new_form"

        google_directory = mod_google_directory[session]

        # Write a JSON to create a new form. Google Forms API compliant
        if create_form_option == "create_new_form":
            # creates a single form with just the title
            # https://developers.google.com/forms/api/guides/create-form-quiz#create_a_new_form
            form_title = GetParams("input_")  # type:ignore
            result = GetParams(  # type:ignore # Get variable name where save results
                "result"
            )
            NEW_FORM = {
                "info": {
                    "title": f"{form_title}",
                }
            }

            try:
                # Create the form
                create_form = (
                    google_directory.form_service.forms()
                    .create(body=NEW_FORM)
                    .execute()
                )

                # Looks for the formID of the recently created form
                get_result = (
                    google_directory.form_service.forms()
                    .get(formId=create_form["formId"])
                    .execute()
                )
                form_link = get_result["responderUri"]
                print(f"The form was created and the link is {form_link}")
                SetVar(result, True)  # type: ignore

            except Exception as e:
                SetVar(result, False)  # type: ignore
                PrintException()  # type:ignore
                raise e

    if module == "read_form":
        # this collects the metadata of the form.
        # https://developers.google.com/forms/api/guides/retrieve-forms-responses#retrieve_form_contents_and_metadata
        form_id = GetParams("input_1")  # type: ignore
        result = GetParams(  # type:ignore # Get variable name where save results
            "result"
        )

        google_directory = mod_google_directory[session]

        try:
            # Read the form
            read_form = (
                google_directory.form_service.forms().get(formId=form_id).execute()
            )

            # Store the content in the result var
            SetVar(result, read_form)  # type: ignore
        except Exception as e:
            PrintException()  # type: ignore
            raise e

    if module == "retrieve_responses":
        # https://developers.google.com/forms/api/guides/retrieve-forms-responses#retrieve_all_form_responses
        form_id = GetParams("input_1")  # type: ignore
        result = GetParams(  # type:ignore # Get variable name where save results
            "result"
        )  # type:ignore # Get variable name where save results

        google_directory = mod_google_directory[session]

        try:
            responses = (
                google_directory.form_service.forms()
                .responses()
                .list(formId=form_id)
                .execute()
            )
            SetVar(result, responses)  # type:ignore

        except Exception as e:
            PrintException()  # type: ignore
            raise e

except Exception as e:
    exec("PrintException()")
    raise e
