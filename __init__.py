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

# import sys # it's already in rocketbot main

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"]  # type:ignore
google_directory_path = os.path.join(base_path, "modules", "GoogleForms")
gd_libs_path = os.path.join(google_directory_path, "libs")  # type:ignore

if gd_libs_path not in sys.path:
    sys.path.append(gd_libs_path)

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
        self.SCOPES = "https://www.googleapis.com/auth/forms.body"
        self.DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
        self.credential_path = credential_path
        self.form_service = None

    def config_credentials(self):
        """Configure the credentials."""
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient import discovery

        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if not self.creds or self.creds.invalid:
            flow = InstalledAppFlow.from_client_secrets_file(
                self.credential_path, self.SCOPES
            )
            self.creds = flow.run_local_server()
            # If there are no (valid) credentials available, let the user log in.
            # Save the credentials for the next run
            # with open(self.token_path, "w") as token:
            #     token.write(self.creds.to_json())

        print("deberia imprimir esta linea")
        print(self.creds)
        self.form_service = discovery.build("forms", "v1", credentials=self.creds)
        # print("no deberia imprimir esta linea")


try:
    # Get data from robot
    module = GetParams("module")  # type:ignore # Get command executed
    session = GetParams("session")  # type:ignore # Get Session name
    result = GetParams("result")  # type:ignore # Get variable name where save results

    if not session:
        session = SESSION_DEFAULT  # Set default session

    if module == "connect_forms":
        credentials_path = GetParams("credentials_path")  # type:ignore

        google_directory = GoogleDirectory(credentials_path)

        try:
            google_directory.config_credentials()
            mod_google_directory[session] = google_directory
            SetVar(result, True)  # type:ignore

            # Esto es una prueba para ver si lo crea bien------------------------
            # Request body for creating a form
            NEW_FORM = {
                "info": {
                    "title": "fomulario nuevo",
                }
            }

            NEW_QUESTION = {
                "requests": [
                    {
                        "createItem": {
                            "item": {
                                "title": "In what year did the United States land a mission on the moon?",
                                "questionItem": {
                                    "question": {
                                        "required": True,
                                        "choiceQuestion": {
                                            "type": "RADIO",
                                            "options": [
                                                {"value": "1965"},
                                                {"value": "1967"},
                                                {"value": "1969"},
                                                {"value": "1971"},
                                            ],
                                            "shuffle": True,
                                        },
                                    }
                                },
                            },
                            "location": {"index": 0},
                        }
                    }
                ]
            }

            # Creates the initial form
            result = google_directory.form_service.forms().create(body=NEW_FORM).execute()

            # Adds the question to the form
            question_setting = (
                google_directory.form_service.forms()
                .batchUpdate(formId=result["formId"], body=NEW_QUESTION)
                .execute()
            )

            # Prints the result to show the question has been added
            get_result = google_directory.form_service.forms().get(formId=result["formId"]).execute()
            print(get_result)


            # fin de la prueba ---------------------------------------------------

        except Exception as e:
            SetVar(result, False)  # type:ignore
            print(f'imprimio False en la variable "{result}"')
            PrintException()  # type:ignore
            raise e

        
    if module == "list_form":
        print(f"The module {module} is not yet implemented")
        pass

    if module == "read_form":
        print(f"The module {module} is not yet implemented")
        pass

    if module == "create_form":
        print(f"The module {module} is not yet implemented")

        # Request body for creating a form
        NEW_FORM = {
            "info": {
                "title": "fomulario nuevo",
            }
        }

        NEW_QUESTION = {
            "requests": [
                {
                    "createItem": {
                        "item": {
                            "title": "In what year did the United States land a mission on the moon?",
                            "questionItem": {
                                "question": {
                                    "required": True,
                                    "choiceQuestion": {
                                        "type": "RADIO",
                                        "options": [
                                            {"value": "1965"},
                                            {"value": "1967"},
                                            {"value": "1969"},
                                            {"value": "1971"},
                                        ],
                                        "shuffle": True,
                                    },
                                }
                            },
                        },
                        "location": {"index": 0},
                    }
                }
            ]
        }

        # Creates the initial form
        result = google_directory.form_service.forms().create(body=NEW_FORM).execute()

        # Adds the question to the form
        question_setting = (
            form_service.forms()
            .batchUpdate(formId=result["formId"], body=NEW_QUESTION)
            .execute()
        )

        # Prints the result to show the question has been added
        get_result = form_service.forms().get(formId=result["formId"]).execute()
        print(get_result)

    if module == "delete_form":
        print(f"The module {module} is not yet implemented")
        pass

    if module == "export_to_xlsx":
        print(f"The module {module} is not yet implemented")
        pass

except Exception as e:
    exec("PrintException()")
    raise e
