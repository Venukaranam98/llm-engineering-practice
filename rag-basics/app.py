import chromadb

with open("notes.txt", "r") as file:
    text = file.read()

client = chromadb.Client()

collection = client.create_collection(
    name="ekart_notes"
)

collection.add(
    documents=[text],
    ids=["1"]
)

question = "Which database does E-Kart use?"

results = collection.query(
    query_texts=[question],
    n_results=1
)

context = results["documents"][0][0]

print("Retrieved Context:")
print(context)