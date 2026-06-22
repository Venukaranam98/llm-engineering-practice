import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="ekart_notes"
)

results = collection.query(
    query_texts=[
        "Which technology is used for background tasks?"
    ],
    n_results=1
)

print(results["documents"])