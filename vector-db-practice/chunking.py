from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
FastAPI is a Python web framework.

Redis is an in-memory database.

PostgreSQL stores structured data.

Celery handles background tasks.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}:")
    print(chunk)
    print("-" * 20)