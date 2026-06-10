from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} briefly"
)

parser = StrOutputParser()

chain = prompt | llm | parser

responses = chain.batch(
    [
        {"topic": "FastAPI"},
        {"topic": "PostgreSQL"},
        {"topic": "JWT"}
    ]
)

for response in responses:
    print(response)
    print("-" * 50)