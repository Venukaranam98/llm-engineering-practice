import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
E-Kart is a full-stack e-commerce application.

Backend technologies:
FastAPI, PostgreSQL, Redis, Celery.

Frontend technologies:
React, JavaScript.

Features:
JWT Authentication, Razorpay Integration,
Product Search, Category Filtering.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

client = chromadb.Client()

collection = client.create_collection(
    name="ekart_rag"
)
print(chunks)
collection.add(
    documents=chunks,
    ids=[str(i) for i in range(len(chunks))]
)

results = collection.query(
    query_texts=[
        "What is Celery used for?"
    ],
    n_results=1
)

print(results["documents"])