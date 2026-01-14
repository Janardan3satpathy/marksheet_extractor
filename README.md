AI Marksheet Extractor API

A FastAPI-based extraction service that uses \*\*Google Gemini 1.5 Flash\*\* to extract structured data (candidate details, subject marks, grades) from marksheet images and PDFs.

🚀 Features  
\- Multimodal Extraction: Supports \`.pdf\`, \`.jpg\`, \`.png\`.  
\- Structured JSON:Returns consistent schema validated by Pydantic.  
\- Confidence Scoring: AI assesses visual clarity for every field.  
\- Robust: Handles tables and complex layouts using Vision LLM capabilities.

 🛠 Tech Stack  
\-Framework: FastAPI  
\- AI Model: Gemini 1.5 Flash  
\- PDF Processing: pdf2image / Poppler  
\- Validation: Pydantic

⚙️ Setup & Installation

1.Clone the repo  
   \`\`\`bash  
   git clone \<repo-url\>  
   cd marksheet-extractor

2. **Install System Dependencies (Poppler)**  
   * **Mac:** `brew install poppler`  
   * **Linux:** `sudo apt-get install poppler-utils`  
   * **Windows:** Download binary and add to PATH.

**Install Python Dependencies**  
Bash  
pip install \-r requirements.txt

3. 

**Environment Variables** Create a `.env` file and add your Google API Key:  
GOOGLE\_API\_KEY=your\_key\_here

4. 

**Run the Server**  
Bash  
uvicorn app.main:app \--reload

5.   
6. **Test** Open `http://localhost:8000/docs` to use the Swagger UI and upload a file.

## **🧠 Approach Note**

We utilized a **Vision-LLM (Gemini 1.5)** rather than traditional OCR (Tesseract) because marksheets often contain complex table structures that standard OCR flattens incorrectly. The Vision model "sees" the row/column alignment, ensuring marks are attributed to the correct subject.

