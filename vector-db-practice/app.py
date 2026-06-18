import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="learning_notes"
)

collection.add(
    documents=[
        "FastAPI is a Python web framework",
        "Redis is an in-memory database",
        "PostgreSQL is a relational database",
        "Celery handles background tasks",
        "JWT is used for authentication",
        "PostgreSQL stores structured data"
    ],
    ids=["1", "2", "3", "4", "5", "6"]
)

results = collection.query(
    query_texts=[
        "Which technologies are used in backend development?"
    ],
    n_results=3
)

print(results["documents"])