from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

text = "FastAPI is a Python framework"

embedding = model.encode(text)

print("Vector Length:", len(embedding))

print("\nFirst 10 Values:")

print(embedding[:10])