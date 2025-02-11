



# Google Forms
  
Este módulo permite criar, ler e obter respostas do Formulários Google.  

*Read this in other languages: [English](Manual_GoogleForms.md), [Português](Manual_GoogleForms.pr.md), [Español](Manual_GoogleForms.es.md)*
  
![banner](imgs/Banner_GoogleForms.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Cómo usar este modulo

Habilitar a API do Google Forms
1. Acesse o Google Cloud Console. https://console.cloud.google.com/
2. Crie um novo projeto ou selecione um existente.
3. No menu lateral, vá para "APIs e Serviços" > "Biblioteca".
4. Pesquise por "Google Forms API" e clique em Habilitar.

Configurar tela de consentimento
1. Vá para "API e Serviços" > "Configurar tela de consentimento".
2. Escolha o tipo de usuário:
Interno → Somente usuários da sua organização (se você usar um domínio do Google Workspace).
Externo → Qualquer usuário com uma conta do Google pode acessar (requer aprovação do Google para produção).
3. Clique em "Criar".
4. Informações básicas completas:
Nome do aplicativo → Insira um nome para identificar seu aplicativo.
E-mail de suporte ao desenvolvedor → Insira seu e-mail de contato.
5. Clique em "Salvar e continuar".
6. Usuários de teste: adicione os e-mails dos usuários que poderão testar a API.

Criar Credenciais
1. Vá para "APIs e Serviços" > 
"Credenciais".
2. Clique em "Criar Credenciais" > "ID do Cliente OAuth".
3. Defina o tipo de aplicação: selecione "Área de Trabalho".
4. Baixe o arquivo credentials.json e salve-o no seu projeto.
## Descrição do comando

### Connect with G-Forms
  
Connect with Google Forms
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho de credenciais|Arquivo JSON com as credenciais de acesso ao API do Google Forms. Veja a documentação para obter mais informações.|C:\Usuario\Desktop\credentials.json|
|Porto (Opcional)||8080|
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|
|Connect with google forms will load the credentials files as indicated by the first field. Afterwards, in a success case the bot will write True in the designated variable|||

### Create Form
  
Create a new form using the title given
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Form title||My form title|
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|
|This command will create a form with a title specified on the field, in a success case the bot will write True in the designated variable|||

### Read Form
  
This collects the metadata of the form
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|FormID||FormID|
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|
|This command will read the metadata of the form. You have to specify the FormID, which is found inbetween /d/ and /edit/ part of the link.|||
|For example, for this link https//docs.google.com/forms/d/168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w/edit the id is 168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w|||
|Afterwards, the return will be stored in the variable called|||

### Retrieve responses
  
Retrieve the responses of a form
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|FormID||FormID|
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|
|This command collects all the responses sent to a form by a certain FormID. You have to specify the FormID, which is found inbetween /d/ and /edit/ part of the link|||
|For example, for this link https//docs.google.com/forms/d/168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w/edit the id is 168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w|||
|Afterwards, the return will be stored in the variable called|||
