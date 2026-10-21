from langchain_chroma import Chroma

from app.config import embeddings
from app.ingest import DB_DIR


def get_retriever():
    """Return a retriever for indexed company documents."""

    vector_store = Chroma(
        collection_name="enterprise_documents",
        embedding_function=embeddings,
        persist_directory=DB_DIR,
    )

    return vector_store.as_retriever(
        search_kwargs={"k": 4}
    )