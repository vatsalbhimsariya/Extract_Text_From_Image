import logging
import easyocr
import json
import azure.functions as func

def main(blob: func.InputStream, outputBlob: func.Out[str]) -> None:
    reader = easyocr.Reader(['en'])
    img_bytes = blob.read()
    results = reader.readtext(img_bytes)

    # Prepare data as JSON (list of dicts)
    output_data = [
        {
            "bbox": res[0],
            "text": res[1],
            "confidence": res[2]
        }
        for res in results
    ]

    # Convert to JSON string
    output_json = json.dumps(output_data, indent=4)

    # Write JSON string to output blob
    outputBlob.set(output_json)

    logging.info(f"Processed blob {blob.name} and saved OCR results to output-json container.")
