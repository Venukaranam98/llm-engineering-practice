from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

documents = [
    Document(page_content="FastAPI is a modern Python framework."),
    Document(page_content="JWT is used for authentication."),
    Document(page_content="PostgreSQL is a relational database.")
]

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

prompt = PromptTemplate.from_template(
"""
Answer the question using the context below.

Context:
{context}

Question:
{question}
"""
)

llm = ChatGroq(model="llama-3.3-70b-versatile")
parser = StrOutputParser()
chain = prompt | llm | parser

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    if not docs:
        print("\nAI: Sorry, I couldn't find relevant information.")
        continue

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    response = chain.invoke({
        "context": context,
        "question": question
    })

    print("\nAI:", response)