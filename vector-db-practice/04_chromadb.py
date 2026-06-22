from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
import chromadb

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

texts = [chunk.page_content for chunk in chunks]

vectors = embedding_model.embed_documents(texts)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="ekart_notes"
)

collection.add(
    documents=texts,
    embeddings=vectors,
    ids=[str(i) for i in range(len(texts))]
)

print("Documents stored successfully!")
print(f"Total stored documents: {collection.count()}")