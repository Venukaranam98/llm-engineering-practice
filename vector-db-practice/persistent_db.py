import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection_name = "learning_notes"

try:
    collection = client.get_collection(
        name=collection_name
    )
    print("Collection loaded.")
except:
    collection = client.create_collection(
        name=collection_name
    )

    collection.add(
        documents=[
            "FastAPI is a Python web framework",
            "Redis is an in-memory database",
            "PostgreSQL stores structured data",
            "Celery handles background tasks"
        ],
        ids=["1", "2", "3", "4"]
    )

    print("Collection created and data added.")

results = collection.query(
    query_texts=[
        "Which tool handles asynchronous jobs?"
    ],
    n_results=1
)

print(results["documents"])