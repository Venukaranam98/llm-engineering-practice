from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": "Return ONLY valid JSON"
        },
        {
            "role": "user",
            "content": """
            Analyze this student

            Name: Venu
            Skills: Python, FastAPI, React

            Return:
            name
            skills
            level
            """
        }
    ]
)

print(response.choices[0].message.content)