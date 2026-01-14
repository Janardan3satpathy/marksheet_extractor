import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from app.schemas import ExtractionResponse

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# We use the Flash model for speed and cost-efficiency
MODEL_NAME = "gemini-1.5-flash"

SYSTEM_PROMPT = """
You are an expert Document AI extractor. 
Analyze the uploaded marksheet image and extract data strictly matching the provided JSON schema.

Rules:
1. Extract Candidate Name, Roll No, Institution, and Subject-wise marks accurately.
2. If a field is missing or illegible, return null.
3. Normalize grades to Uppercase.
4. Confidence Score: Assign 0.0 to 1.0 based on text clarity (1.0 = clear, <0.5 = blurry/handwritten).
5. Output must be raw JSON. Do not include markdown formatting like ```json.
"""

def extract_marksheet_data(image_input) -> dict:
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        
        # We prompt the model to generate text that matches our schema structure
        # Note: Gemini 1.5 supports explicit JSON mode, but prompting with schema examples is robust.
        
        response = model.generate_content(
            [
                SYSTEM_PROMPT,
                f"Output Schema Reference: {ExtractionResponse.model_json_schema()}",
                image_input
            ],
            generation_config={"response_mime_type": "application/json"}
        )
        
        # Parse the JSON string response
        raw_json = json.loads(response.text)
        
        # Validate against Pydantic model to ensure type safety
        validated_data = ExtractionResponse(**raw_json)
        
        return validated_data.dict()

    except Exception as e:
        print(f"LLM Error: {e}")
        raise RuntimeError("Failed to extract data from the AI model.")