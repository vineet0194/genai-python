# Zero Shot Prompting

# Zero-shot prompting means asking the model to perform a task without giving it any examples of how to do it.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# first line set as "\" allows you to strip the very first newline 
# (as triple quotes preserve chars) so the first line wont be a wasted token

SYSTEM_PROMPT = '''\
You are an expert in Maths and you should only answer Math related questions.
If you receive an input that is not related, just apologise and do not answer it.
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
            "content": "What is the sum of first n odd numbers?"
        },
        {
            "role": "user",                             # answered in same response
            "content": "how many As in AAAAAA?"
        }
    ]
)

print(response.choices[0].message.content)