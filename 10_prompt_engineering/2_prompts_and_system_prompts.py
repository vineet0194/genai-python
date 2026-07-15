import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "system",
            "content": "You are an expert in Maths and you should only answer Math related questions. If you receive an input that is not related, just apologise and do not answer it."
        },
        {
            "role": "user",
            "content": "What is the sum of first n odd numbers?"
        }
    ]
)

print(response.choices[0].message.content)