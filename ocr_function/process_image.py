import os
from azure.storage.blob import BlobServiceClient
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from send_email import send_email
from config import *

def process_image_from_blob(blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONN_STRING)
    blob_client = blob_service_client.get_blob_client(container=INPUT_CONTAINER, blob=blob_name)
    image_stream = blob_client.download_blob().readall()

    client = DocumentAnalysisClient(endpoint=VISION_ENDPOINT, credential=AzureKeyCredential(VISION_KEY))
    poller = client.begin_analyze_document("prebuilt-read", document=image_stream)
    result = poller.result()

    text_data = {
        "file": blob_name,
        "text": [line.content for page in result.pages for line in page.lines]
    }

    output_blob_name = blob_name.rsplit(".", 1)[0] + ".json"
    output_blob_client = blob_service_client.get_blob_client(container=OUTPUT_CONTAINER, blob=output_blob_name)
    output_blob_client.upload_blob(str(text_data), overwrite=True)

    send_email(subject="OCR Completed", body=f"OCR for '{blob_name}' done. JSON: {output_blob_name}")