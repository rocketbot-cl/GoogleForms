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

    def config_credentials(self):
        """Configure the credentials."""
        from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore
        from googleapiclient import discovery  # type: ignore

        self.creds = None

        if not self.creds or self.creds.invalid:
            flow = InstalledAppFlow.from_client_secrets_file(
                self.credential_path, self.SCOPES
            )
            self.creds = flow.run_local_server()

        self.form_service = discovery.build("forms", "v1", credentials=self.creds)


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

        except Exception as e:
            SetVar(result, False)  # type:ignore
            PrintException()  # type:ignore
            raise e

    if module == "create_form":
        # The field "input_" is left intentionally to catch up with the if cycle.
        # Just after the if is confirmed a function GetParams is called and stored in a meaningful variable
        # create_form_option = GetParams("option_")

        """
        For faster fixing, I set constant the option to create form
        Please delete this harcode before implementing the othe methods
        module == "duplicate_a_form" and module == "convert_form_to_quiz"
        """
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

        """
        # task suspended by new priorities
        if create_form_option == "duplicate_a_form":
            # https://developers.google.com/forms/api/guides/create-form-quiz#duplicate_an_existing_form
            form_id = GetParams("input_") #type: ignore
            copied_file = {'title': 'my_copy'}
            print(dir(google_directory.form_service))

            result = (
                google_directory.form_service.files()
                .copy(fileId=form_id, body=copied_file)
                .execute()
            )

            # Prints the result to show the form has been created
            get_result = google_directory.form_service.forms()
            print(get_result)
        """

        """
        # task suspended by new priorities
        if create_form_option == "convert_form_to_quiz":
            # https://developers.google.com/forms/api/guides/create-form-quiz#convert_a_form_to_a_quiz
            form_id = GetParams("input_") #type: ignore
        """

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

    """
    # this module is not even written in the package.json!
    if module == "add_question":
        print(f"The module {module} is not yet implemented")
        pass

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

        # Adds the question to the form
        question_setting = (
            google_directory.form_service.forms()
            .batchUpdate(formId=result["formId"], body=NEW_QUESTION)
            .execute()
        )
    """

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
    """
    # task suspended by new priorities
    if module == "delete_form":
        print(f"The module {module} is not yet implemented")
    """

    """
    # task suspended by new priorities
    if module == "export_to_xlsx":
        print(f"The module {module} is not yet implemented")
    """

except Exception as e:
    exec("PrintException()")
    raise e
