from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model,
    collection_name="metadata_demo"
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 1}
)

results = retriever.invoke(
    "Which technology is used for background tasks?"
)

for doc in results:
    print(doc.page_content)
    print(doc.metadata)