from langchain_core.documents import Document

from langchain_chroma import Chroma

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

documents = [

    Document(
        page_content="FastAPI is a Python framework."
    ),

    Document(
        page_content="JWT is used for authentication."
    ),

    Document(
        page_content="PostgreSQL is a relational database."
    )

]

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    persist_directory="./chroma_db"
)

results = vector_store.similarity_search(
    "How do login tokens work?",
    k=1
)

print(results[0].page_content)