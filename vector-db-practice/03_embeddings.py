from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

loader = PyPDFLoader("notes.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectors = embedding_model.embed_documents(
    [chunk.page_content for chunk in chunks]
)

print(f"Total chunks: {len(chunks)}")
print(f"Total vectors: {len(vectors)}")
print(f"Vector dimensions: {len(vectors[0])}")