from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

text = """
FastAPI is a modern Python framework.

It is used for building APIs.

It supports automatic documentation.

It is very fast and easy to learn.

JWT is used for authentication.

PostgreSQL is a powerful database.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)