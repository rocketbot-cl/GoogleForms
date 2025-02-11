



# Google Forms
  
Este módulo le permite crear, leer y obtener respuestas de Google Forms.  

*Read this in other languages: [English](Manual_GoogleForms.md), [Português](Manual_GoogleForms.pr.md), [Español](Manual_GoogleForms.es.md)*
  
![banner](imgs/Banner_GoogleForms.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Cómo usar este modulo

Habilitar la API de Google Forms
1. Ir a la Google Cloud Console https://console.cloud.google.com/
2. Crear un nuevo proyecto o seleccionar uno existente.
3. En el menú lateral, ir a "API y Servicios" > "Biblioteca".
4. Buscar "Google Forms API" y hacer clic en Habilitar.

Configurar pantalla de consentimiento
1. Ir a "API y Servicios" > "Configurar pantalla de consentimiento".
2. Elige el tipo de usuario:
Interno → Solo usuarios de tu organización (si usas un dominio de Google Workspace).
Externo → Cualquier usuario con una cuenta de Google puede acceder (requiere aprobación de Google para producción).
3. Haz clic en "Crear".
4. Completar Información Básica: 
Nombre de la aplicación → Escribe un nombre para identificar tu app.
Correo electrónico de soporte del desarrollador → Ingresa tu correo de contacto.
5. Haz clic en "Guardar y Continuar".
6. Usuarios de prueba: agrega los correos electrónicos de los usuarios que podrán probar la API.


Crear 
Credenciales
1. Ir a "API y Servicios" > "Credenciales".
2. Hacer clic en "Crear credenciales" > "ID de cliente de OAuth".
3. Configurar el tipo de aplicación: selecciona "Escritorio".
4. Descargar el archivo credentials.json y guárdalo en tu proyecto.


## Descripción de los comandos

### Conectar con Fomularios de Google
  
Conectar con Formularios de Google
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo de credenciales|Archivo JSON con las credenciales de acceso a la API de Google Forms. Revisar la documentación para obtener más información.|C:\Usuario\Desktop\credenciales.json|
|Puerto (Opcional)||8080|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|
|Conectar con formularios cargará el archivo según la ruta del archivo de credenciales y se conectará con Google Forms. En caso de éxito grabará True en la variable designada para grabar el resultado|||

### Crear Formulario
  
Crear un Formulario de Google
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Título del Form||Mi título de Form|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|
|Este comando creará un nuevo formulario cuyo título es el del primer campo. En caso de éxito grabara True en la variable indicada|||

### Leer Formulario
  
Junta los datos propios formulario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|FormID||FormID|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|
|Este commando buscara la metadata del form. Para eso se necesita especificar el FormID, el cual se encuentra en el link, despues de /d/ y antes de /edit|||
|Por ejemplo, en https//docs.google.com/forms/d/168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w/edit el id es 168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w|||
|Luego, se guardará la informacion en la variable indicada|||

### Recolectar respuestas
  
Recolecta las respuestas del formulario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|FormID||FormID|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|
|Este comando junta todas las respuestas enviadas al formulario, segun su correspondiente FormID. El FormID se encuentra en el link, despues de /d/ y antes de /edit|||
|Por ejemplo, en https//docs.google.com/forms/d/168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w/edit el id es 168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w|||
|Luego, se guardará la informacion en la variable indicada|||
