from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a senior Python mentor."
        ),
        (
            "human",
            "Explain {topic} in simple words."
        )
    ]
)


parser = StrOutputParser()


chain = prompt | llm | parser


response = chain.invoke(
    {
        "topic": "FastAPI"
    }
)


print(response)