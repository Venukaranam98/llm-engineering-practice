# RAG Basics Notes

## What is RAG?

RAG stands for:

Retrieval Augmented Generation

Purpose:

* Retrieve relevant information from documents
* Provide accurate answers using external knowledge

Pipeline:

PDF
↓
Loader
↓
Chunks
↓
Embeddings
↓
Vector Database
↓
Retriever
↓
LLM
↓
Answer

---

## Document Loader

A Document Loader loads files and converts them into LangChain Document objects.

Examples:

* TextLoader()
* PyPDFLoader()
* Docx2txtLoader()

Document Structure:

Document(
page_content="Actual text",
metadata={}
)

page_content -> Contains document text

metadata -> Contains extra information like source and page number

Purpose:

* Extract text from files
* Convert files into LangChain Documents

---

## Chunking

Chunking means splitting a large document into smaller pieces.

Benefits:

* Better retrieval
* Faster search
* Lower token usage
* More accurate answers

Example:

PDF
↓
Chunks
↓
Embeddings
↓
Vector Database

---

## Chunk Size

chunk_size controls the maximum size of each chunk.

Example:

chunk_size=500

Purpose:

* Control chunk length
* Improve retrieval quality

---

## Chunk Overlap

chunk_overlap keeps some content from the previous chunk inside the next chunk.

Example:

chunk_overlap=50

Purpose:

* Preserve context
* Prevent information loss
* Improve retrieval quality

Example:

Chunk 1:
FastAPI supports JWT

Chunk 2:
supports JWT authentication

This prevents context loss.

---

## Embeddings

Embeddings are numerical vector representations of text.

Purpose:

* Capture meaning
* Understand semantic relationships
* Enable semantic search

Example:

Text:

FastAPI

Vector:

[0.12, -0.45, 0.89, ...]

Flow:

Text
↓
Embedding Model
↓
Vector

---

## Cosine Similarity

Cosine Similarity measures how similar two vectors are.

Range:

1.0 → Very Similar

0.0 → Unrelated

-1.0 → Opposite Meaning

Example:

Car vs Automobile

Similarity Score:

0.8645

Meaning:

The two words are semantically similar.

---

## Semantic Search

Semantic Search searches by meaning instead of exact words.

Example:

Document:

Automobile

User Query:

Car

Keyword Search:

No Match

Semantic Search:

Match Found

Reason:

Car ≈ Automobile

---

## ChromaDB

ChromaDB is a Vector Database.

Purpose:

* Store embeddings
* Store documents
* Store metadata
* Perform similarity search

Example:

Document:
JWT is used for authentication

Embedding:
[0.12, 0.45, ...]

Metadata:
page=2

---

## Vector Store

A Vector Store is a database designed to store embeddings and perform similarity search.

Examples:

* ChromaDB
* Pinecone
* FAISS
* Qdrant
* Weaviate

Think:

PostgreSQL → Stores Rows

ChromaDB → Stores Vectors

---

## Similarity Search

Similarity Search retrieves the most relevant chunks based on meaning.

Flow:

User Query
↓
Embedding
↓
Compare With Stored Embeddings
↓
Most Similar Chunk

Example:

Query:

How do login tokens work?

Retrieved Chunk:

JWT is used for authentication

Reason:

The embeddings are semantically similar.

---

---

## Retriever

A Retriever is responsible for fetching the most relevant chunks from a Vector Database based on the user's query.

Purpose:

* Retrieve only relevant chunks
* Reduce token usage
* Improve answer quality
* Avoid sending the entire database to the LLM

Flow:

User Query
↓
Embedding
↓
Retriever
↓
Relevant Chunks

Example:

Stored Chunks:

Chunk 1 → FastAPI

Chunk 2 → JWT Authentication

Chunk 3 → PostgreSQL

User Query:

How do login tokens work?

Retrieved Chunk:

JWT Authentication

Reason:

The retrieved chunk has the highest semantic similarity with the user's query.

---

## Why Retriever is Important

Without Retriever:

10,000 Chunks
↓
Send Everything To LLM

Problems:

* Expensive
* Slow
* Token Limit Issues

With Retriever:

10,000 Chunks
↓
Top Relevant Chunks
↓
LLM

Benefits:

* Faster
* Cheaper
* More Accurate

---

## Complete RAG Pipeline

A Complete RAG Pipeline combines retrieval and generation.

Flow:

User Question
↓
Embedding
↓
Retriever
↓
Relevant Chunks
↓
Prompt
↓
LLM
↓
Final Answer

Purpose:

* Retrieve relevant information
* Generate context-aware answers
* Reduce hallucinations

---

## RAG Pipeline Components

1. Document Loader

Loads files into LangChain Documents.

2. Chunking

Splits large documents into smaller chunks.

3. Embeddings

Converts text into vectors.

4. ChromaDB

Stores vectors and metadata.

5. Retriever

Fetches relevant chunks.

6. Prompt

Combines question and retrieved context.

7. LLM

Generates the final answer.

---

## Retriever vs ChromaDB

ChromaDB:

* Stores embeddings
* Stores documents
* Stores metadata

Retriever:

* Searches ChromaDB
* Retrieves relevant chunks
* Does not store data

Think:

PostgreSQL → Database

SQL Query → Search

Similarly:

ChromaDB → Vector Database

Retriever → Search Component

---

## RAG Example

Stored Documents:

FastAPI is a Python framework.

JWT is used for authentication.

PostgreSQL is a relational database.

User Question:

How do login tokens work?

Retriever Output:

JWT is used for authentication.

Prompt Sent To LLM:

Context:
JWT is used for authentication.

Question:
How do login tokens work?

Final LLM Answer:

Login tokens are commonly implemented using JWT (JSON Web Tokens). After a user logs in, a JWT token is generated and used to authenticate future requests.

---

## Key Takeaways

* Document Loaders convert files into LangChain Documents.
* Chunking splits large documents into smaller chunks.
* chunk_overlap preserves context between chunks.
* Embeddings convert text into vectors.
* Cosine Similarity measures vector similarity.
* Semantic Search searches by meaning.
* ChromaDB stores vectors, documents, and metadata.
* Vector Stores perform similarity search.
* Similarity Search retrieves relevant chunks using embeddings.
* Retrievers fetch the most relevant chunks from a vector database.
* Complete RAG Pipelines combine retrieval and generation.
* RAG improves accuracy by providing external context to LLMs.

