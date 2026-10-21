# GenAI Knowledge Assistant

A local PDF question-answering app with a FastAPI backend, Streamlit UI, Chroma
vector store, Hugging Face embeddings, and Groq chat completions.

## Setup

1. Create and activate a Python virtual environment, then install dependencies:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and set `GROQ_API_KEY` to your Groq API key.
   Keep `.env` private; it is excluded from Git.

3. Put a PDF you are authorized to use in `data`, then index it:

   ```powershell
   python -c "from app.ingest import ingest_pdf; print(ingest_pdf('data/your-document.pdf'))"
   ```

## Run

Start the API in one terminal:

```powershell
python -m uvicorn app.api:app --host 127.0.0.1 --port 8000
```

Start the UI in a second terminal:

```powershell
python -m streamlit run frontend/streamlit_app.py
```

Open http://localhost:8501. API documentation is available at
http://localhost:8000/docs.