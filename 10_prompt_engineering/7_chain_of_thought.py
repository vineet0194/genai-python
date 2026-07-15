# Chain of Thought Prompting

# CoT means improving a model's reasoning by generating step-by-step reasoning before providing the final answer.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = '''\
You're an expert AI assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
- Strictly follow the given JSON output format
- Only run one step at a time
- The sequences of steps is START(where user gives an input), PLAN (that can be multiple times), and finally OUTPUT (which is going to be displayed to the user)

Output JSON Format:
{
    "step": "START" | "PLAN" | "OUTPUT",
    "content": "string"
}

Example:

Input: 
START: {
  "step": "START",
  "content": "hey, can you solve 2+3*5/10?"
}

Output JSON Format:
PLAN: {
  "step": "PLAN",
  "content": "Identify the mathematical expression and evaluate it using operator precedence (BODMAS/PEMDAS)."
}
PLAN: {
  "step": "PLAN",
  "content": "Evaluate the multiplication: 3 x 5 = 15. The expression becomes 2 + 15 / 10."
}
PLAN: {
  "step": "PLAN",
  "content": "Evaluate the division: 15 / 10 = 1.5. The expression becomes 2 + 1.5."
}
PLAN: {
  "step": "PLAN",
  "content": "Evaluate the remaining addition: 2 + 1.5 = 3.5."
}
OUTPUT: {
  "step": "OUTPUT",
  "content": "3.5"
}
'''

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    response_format={
        "type": "json_object"
    },
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "hey, write a code to add n numbers in javascript"
        }
    ]
)

print(response.choices[0].message.content)

# This is useful for learning or building custom reasoning pipelines.

# ! But this is not how modern reasoning models internally perform Chain-of-Thought.

# Your code is asking the model to expose its reasoning by outputting PLAN steps.
# Modern reasoning models generally perform the reasoning internally and return only the
# final answer unless your application explicitly asks for structured intermediate steps
# like you've done here.