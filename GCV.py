import os
from google.cloud import vision

# Set Google Cloud Credentials (Ensure this is correctly set)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your-service-key.json"

def detect_document_text(image_path):
    """Detects document text in a local image file.
    
    Args:
        image_path (str): Path to a local image file.
    
    Returns:
        str: Extracted text from the image.
    """
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Error: Image file not found at {image_path}")

        client = vision.ImageAnnotatorClient()
        with open(image_path, "rb") as image_file:
            content = image_file.read()
        
        image = vision.Image(content=content)
        response = client.document_text_detection(image=image)

        if response.error.message:
            raise Exception(f"Google Vision API Error: {response.error.message}")

        extracted_text = response.full_text_annotation.text
        return extracted_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    local_image_path = "F:/temp/image.png"

    extracted_text = detect_document_text(local_image_path)
    if extracted_text:
        print("Extracted Text from Image:\n", extracted_text)
    else:
        print("No text found or an error occurred.")
