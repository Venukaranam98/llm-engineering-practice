# RAG Basics Notes

## Document Loader

A Document Loader loads files and converts them into LangChain Document objects.

Examples:

- TextLoader()
- PyPDFLoader()
- Docx2txtLoader()

Document Structure:

Document(
    page_content="Actual text",
    metadata={}
)

page_content -> Contains document text

metadata -> Contains extra information like source and page number

---

## Chunking

Chunking means splitting a large document into smaller pieces.

Benefits:

- Better retrieval
- Faster search
- Lower token usage
- More accurate answers

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

---

## Chunk Overlap

chunk_overlap keeps some content from the previous chunk in the next chunk.

Example:

chunk_overlap=50

Purpose:

- Preserve context
- Prevent information loss
- Improve retrieval quality

---

## Semantic Search

Semantic Search searches by meaning instead of exact words.

Example:

Car ≈ Automobile

Keyword Search may fail.

Semantic Search succeeds using embeddings.