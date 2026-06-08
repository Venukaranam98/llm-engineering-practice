from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "My name is Venu"
        },
        {
            "role": "assistant",
            "content": "Nice to meet you Venu"
        },
        {
            "role": "user",
            "content": "What is my name?"
        }
    ]
)

print(response.choices[0].message.content)