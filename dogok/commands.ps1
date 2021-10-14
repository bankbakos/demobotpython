
az ad app create --display-name "ar-echobot-dev-001" --password "VrQnt5XJ9nF5" --available-to-other-tenants

az deployment group create --resource-group "rg-vfhlivechat-dev-001" --template-file "C:\Users\bbakos2\demobotpython\02.echo-bot\deploymentTemplates\template-with-preexisting-rg.json" --parameters appId="6b312792-8502-478b-91b3-4e9e6f74cd10" appSecret="VrQnt5XJ9nF5" botId="ab-echobot-dev-001" newWebAppName="wa-echobot-dev-001" newAppServicePlanName="asp-echobot-dev-001" appServicePlanLocation="germanywestcentral" --name "bas-echobot-dev-001"

az webapp deployment source config-zip --resource-group "rg-vfhlivechat-dev-001" --name "wa-echobot-dev-001" --src "C:\Users\bbakos2\demobotpython\02.echo-bot.zip"