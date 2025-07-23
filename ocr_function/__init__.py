import logging
import azure.functions as func
from process_image import process_image_from_blob

def main(blob: func.InputStream):
    logging.info(f"Processing blob: {blob.name}")
    process_image_from_blob(blob.name)