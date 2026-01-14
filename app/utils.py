from pdf2image import convert_from_bytes
from PIL import Image
import io

def process_file(file_content: bytes, content_type: str) -> Image.Image:
    """
    Converts PDF bytes or Image bytes into a PIL Image object.
    If PDF, takes the first page.
    """
    if "pdf" in content_type:
        try:
            # Convert first page of PDF to image
            images = convert_from_bytes(file_content, first_page=1, last_page=1)
            if images:
                return images[0]
            else:
                raise ValueError("PDF contains no readable pages.")
        except Exception as e:
            raise ValueError(f"Error processing PDF: {str(e)}")
            
    elif "image" in content_type:
        try:
            return Image.open(io.BytesIO(file_content))
        except Exception as e:
            raise ValueError(f"Invalid image file: {str(e)}")
    
    else:
        raise ValueError("Unsupported file type. Please upload PDF, PNG, or JPG.")