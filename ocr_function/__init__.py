import logging
import azure.functions as func

def main(blob: func.InputStream, outputBlob: func.Out[str]):
    logging.info(f"Processing blob: {blob.name}, Size: {blob.length} bytes")

    # Here you replace this with your OCR logic.
    # For example, dummy text output:
    extracted_text = "Sample OCR Text for " + blob.name

    # Write the extracted text to output blob as JSON string or plain text
    outputBlob.set(extracted_text)

    logging.info(f"Output written to output-json/{blob.name}.json")
