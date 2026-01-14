from fastapi import FastAPI, File, UploadFile, HTTPException
from app.utils import process_file
from app.services.llm_service import extract_marksheet_data
import uvicorn

app = FastAPI(
    title="AI Marksheet Extractor",
    description="Extracts structured data from marksheet images/PDFs using Gemini 1.5 Flash.",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "Marksheet Extractor API is running. Use /extract to upload files."}

@app.post("/extract")
async def extract_data(file: UploadFile = File(...)):
    # 1. Validate File Size (10MB limit)
    MAX_SIZE = 10 * 1024 * 1024
    file_content = await file.read()
    
    if len(file_content) > MAX_SIZE:
        raise HTTPException(status_code=413, detail="File too large. Max size is 10MB.")

    # 2. Process File (Convert PDF/Image to PIL Image)
    try:
        image = process_file(file_content, file.content_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # 3. Send to LLM for Extraction
    try:
        extracted_data = extract_marksheet_data(image)
        return {"status": "success", "data": extracted_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)