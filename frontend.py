import streamlit as st
import requests
import json

st.set_page_config(page_title="Marksheet Extractor AI", page_icon="📄", layout="centered")

st.title("📄 AI Marksheet Extractor")
st.markdown("Upload a marksheet image (JPG/PNG) or PDF to extract data.")

with st.sidebar:
    st.header("Configuration")
    api_url = st.text_input("API Endpoint URL", value="http://localhost:8000/extract")
    st.info("Built with Gemini 1.5 Flash & FastAPI")

uploaded_file = st.file_uploader("Choose a file...", type=['png', 'jpg', 'jpeg', 'pdf'])

if uploaded_file is not None:
    if uploaded_file.type in ['image/png', 'image/jpeg']:
        st.image(uploaded_file, caption='Uploaded Marksheet', use_column_width=True)
    elif uploaded_file.type == 'application/pdf':
        st.info("PDF uploaded successfully.")

    if st.button("🚀 Extract Data", type="primary"):
        with st.spinner("Processing document..."):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                response = requests.post(api_url, files=files, timeout=60)
                
                if response.status_code == 200:
                    result = response.json()
                    st.success("Extraction Complete!")
                    st.json(result['data'])
                else:
                    st.error(f"API Error {response.status_code}: {response.text}")
                    
            except Exception as e:
                 st.error(f"Connection Error: {e}")