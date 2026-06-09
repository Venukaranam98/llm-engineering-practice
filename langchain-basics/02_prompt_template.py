from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words"
)

final_prompt = prompt.format(
    topic="FastAPI"
)

response = llm.invoke(
    final_prompt
)

print(response.content)