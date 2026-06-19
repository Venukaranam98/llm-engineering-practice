from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("notes.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_documents(documents)

print(chunks[0].page_content)
print(chunks[0].metadata)
print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}")
    print(chunk.page_content)
    print(chunk.metadata)