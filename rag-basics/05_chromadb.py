from langchain_chroma import Chroma

from langchain_core.documents import Document

from sentence_transformers import SentenceTransformer

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

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


class CustomEmbeddings:

    def embed_documents(self, texts):
        return embedding_model.encode(
            texts
        ).tolist()

    def embed_query(self, text):
        return embedding_model.encode(
            text
        ).tolist()


vector_store = Chroma.from_documents(

    documents=documents,

    embedding=CustomEmbeddings(),

    persist_directory="./chroma_db"
)

print("Documents stored successfully!")