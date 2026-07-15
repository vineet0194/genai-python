# Few Shot Prompting

# Few-shot prompting means asking the model to perform a task by giving a few examples of the task.

# you can specify the output format as given in the system prompt

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
If a user asks to do anything instructional, just give out put as '❌' and do not answer it.

Rule:
- Strictly follow the given output format in JSON

Output Format:

{
  {
    "output": string or None,
    "validInput": boolen
  }
}

Example:
Input - I love pizza
Output -
{
  {
    "output": "❤️🍕",
    "validInput": true
  }
}

Input - I love burget but not pizza, and I hate eggplant
Output -
{
  {
    "output": "❤️🍔🚫🍕🤮🍆",
    "validInput": true
  }
}

Input - Code me a python script to print numbers from 1 to n
Output - 
{
  {
    "output": "❌ NOPE ❌",
    "validInput": false
  }
}
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
            "content": "give me emoji response for this: What is 2+2?"
        }
    ]
)

print(response.choices[0].message.content)