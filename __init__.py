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
base_path = tmp_global_obj["basepath"] #type:ignore
google_directory_path = os.path.join(base_path, "modules", "GoogleAdmin")
gd_libs_path = os.path.join(google_directory_path, "libs") #type:ignore

if gd_libs_path not in sys.path:
    sys.path.append(gd_libs_path)

"""
To connect to multiple databases, a dictionary is created and stores the instance of each connection.
The syntax is {"session name": {data}}
"""
SESSION_DEFAULT = "default"
try:
    if not mod_google_directory:                #type:ignore
        mod_google_directory = {SESSION_DEFAULT:{}}
except NameError:
    mod_google_directory = {SESSION_DEFAULT:{}}


class GoogleDirectory:
    """Google Authentication Class

    Raises:
        e: _description_
    """

    def __init__(self, credential_path, token_path='token.json') -> None:
        self.SCOPES = "https://www.googleapis.com/auth/forms.body"
        self.DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
        self.credential_path = credential_path
        self.token_path = token_path
        self.form_service = None
    
    def config_credentials(self):
        """Configure the credentials."""
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build

        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.token_path):
            print("Loading credentials from token.json")
            self.creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credential_path, self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.token_path, 'w') as token:
                token.write(self.creds.to_json())

        self.form_service = build('forms', 'directory_v1', credentials=self.creds)


try:
    # Get data from robot
    module = GetParams("module")                    #type:ignore # Get command executed 
    session = GetParams("session")                  #type:ignore # Get Session name
    result = GetParams("result")                    #type:ignore # Get variable name where save results
    if not session:
        session = SESSION_DEFAULT # Set default session
    
    if module == 'connect_forms':
        credentials_path = GetParams('credentials_path') #type:ignore
        print(google_directory_path)
        
        google_directory = GoogleDirectory(
            credentials_path,
            os.path.join(google_directory_path, "token.json")
        )

        try:
            google_directory.config_credentials()
            mod_google_directory[session] = google_directory
            SetVar(result, True)                    #type:ignore
        except Exception as e:
            SetVar(result, False)                   #type:ignore
            PrintException()
            raise e


except Exception as e:
    exec('PrintException()')
    raise e
