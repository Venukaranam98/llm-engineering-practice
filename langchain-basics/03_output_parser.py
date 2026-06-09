from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser = StrOutputParser()

response = llm.invoke(
    "What is FastAPI?"
)

clean_response = parser.invoke(
    response
)

print(clean_response)