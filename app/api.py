import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.graph import ask_question
from app.ingest import ingest_pdf

logger = logging.getLogger(__name__)

app = FastAPI(title="GenAI Knowledge Assistant")


class QuestionRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def read_root():
    return {"message": "Welcome to the GenAI Knowledge Assistant API. Visit /docs for documentation."}

@app.post("/ask")
def ask(request: QuestionRequest):
    try:
        return ask_question(request.question)
    except Exception as exc:
        logger.exception("Failed to answer question")
        raise HTTPException(
            status_code=500,
            detail="Unable to answer the question. Check the server logs.",
        ) from exc