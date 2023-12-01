



# Google Forms
  
This module allows you to create, read and get responses of Google Forms.  

*Read this in other languages: [English](Manual_GoogleForms.md), [Português](Manual_GoogleForms.pr.md), [Español](Manual_GoogleForms.es.md)*
  
![banner](imgs/Banner_GoogleForms.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect with G-Forms
  
Connect with Google Forms
|Parameters|Description|example|
| --- | --- | --- |
|Credentials file path|JSON file with the credentials to access the Google Forms API. See the documentation for more information.|C:\User\Desktop\credentials.json|
|Port (Optional)||8080|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|
|Connect with google forms will load the credentials files as indicated by the first field. Afterwards, in a success case the bot will write True in the designated variable|||

### Create Form
  
Create a new form using the title given
|Parameters|Description|example|
| --- | --- | --- |
|Form title||My form title|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|
|This command will create a form with a title specified on the field, in a success case the bot will write True in the designated variable|||

### Read Form
  
This collects the metadata of the form
|Parameters|Description|example|
| --- | --- | --- |
|FormID||FormID|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|
|This command will read the metadata of the form. You have to specify the FormID, which is found inbetween /d/ and /edit/ part of the link.|||
|For example, for this link https//docs.google.com/forms/d/168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w/edit the id is 168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w|||
|Afterwards, the return will be stored in the variable called|||

### Retrieve responses
  
Retrieve the responses of a form
|Parameters|Description|example|
| --- | --- | --- |
|FormID||FormID|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|
|This command collects all the responses sent to a form by a certain FormID. You have to specify the FormID, which is found inbetween /d/ and /edit/ part of the link|||
|For example, for this link https//docs.google.com/forms/d/168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w/edit the id is 168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w|||
|Afterwards, the return will be stored in the variable called|||
