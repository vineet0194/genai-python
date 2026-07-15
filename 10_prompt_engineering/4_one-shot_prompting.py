# One Shot Prompting

# One-shot prompting means asking the model to perform a task by giving exactly one example of the task.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = '''\
You might receive a non-instructional sentence as an input.
Your only task is to convert it into an emoji based on the meaning of the sentence.
If a user asks to do anything instructional, just give out put as "❌ - not allowed" and do not answer it.
Example:
Input - I love pizza
Output - ❤️🍕
'''

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "I love burger but I don't like pizza. What do you like?"
        }
    ]
)

print(response.choices[0].message.content)