# Azure OCR Automation Pipeline (Python)

This repository sets up a private, automated OCR pipeline using Azure Functions and Azure AI Vision. It:
- Extracts handwritten/printed text from images
- Triggers on blob upload to "input-images"
- Stores output JSON to "output-jsons"
- Sends email alerts via SendGrid

## 🛠 Components
- Azure Function App (Python)
- Azure Blob Storage
- Azure AI Vision (Form Recognizer)
- SendGrid Email Notification
- VNet & Private Endpoint ready setup
- ARM Template included

## 🚀 Deployment

```bash
az deployment group create \
  --resource-group <your-rg> \
  --template-file azure-deploy.json \
  --parameters functionAppName=myocrfunc storageAccountName=mystorageacct cognitiveAccountName=myvisionacct
```

## 📂 Function Code

Deploy the `/ocr_function` folder as a zip to your Azure Function App.