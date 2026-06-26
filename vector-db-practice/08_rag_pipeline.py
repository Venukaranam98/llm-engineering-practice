from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate 
from dotenv import load_dotenv
import os

load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    collection_name="metadata_demo",
    embedding_function=embedding_model,
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

question = "Which technologies are used in the backend?"

docs = retriever.invoke(question)

context = "\n\n".join(
    [doc.page_content for doc in docs]
)

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""
)

chain = prompt | llm

response = chain.invoke(
    {
        "context": context,
        "question": question
    }
)

print(response.content)