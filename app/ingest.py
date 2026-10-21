from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import embeddings

DATA_DIR = Path("data")
DB_DIR = "chroma_db"


def ingest_pdf(pdf_path: str) -> int:
    """Load a PDF, split it into chunks, and index the chunks."""

    path = Path(pdf_path)

    if not path.exists() or path.suffix.lower() != ".pdf":
        raise ValueError("Provide a valid PDF file.")

    documents = PyPDFLoader(str(path)).load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
    )

    chunks = splitter.split_documents(documents)

    for chunk in chunks:
        chunk.metadata["source"] = path.name

    if not chunks:
        raise ValueError("No extractable text found in this PDF.")

    vector_store = Chroma(
        collection_name="enterprise_documents",
        embedding_function=embeddings,
        persist_directory=DB_DIR,
    )

    vector_store.add_documents(chunks)

    return len(chunks)