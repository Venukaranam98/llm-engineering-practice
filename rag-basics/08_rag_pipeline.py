from dotenv import load_dotenv
import os

from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


documents = [

    Document(
        page_content="FastAPI is a modern Python framework."
    ),

    Document(
        page_content="JWT is used for authentication."
    ),

    Document(
        page_content="PostgreSQL is a relational database."
    )

]

# Embedding Model

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding
)

retriever = vector_store.as_retriever()
question = "How do login tokens work?"

docs = retriever.invoke(question)


context = "\n".join(
    [doc.page_content for doc in docs]
)


prompt = PromptTemplate.from_template(
    """
Answer the question using only the context below.

Context:
{context}

Question:
{question}
"""
)


llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke(
    {
        "context": context,
        "question": question
    }
)

print("\nQuestion:")
print(question)

print("\nRetrieved Context:")
print(context)

print("\nAnswer:")
print(response)