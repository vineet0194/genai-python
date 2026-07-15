import os
import json
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
- Your response MUST consist of exactly one valid JSON object.
- Do not output any text before or after the JSON.
- Do not explain your reasoning outside the JSON.
- Do not apologize.
- Do not revise previous outputs.- Never emit multiple JSON objects.
- Only run one step at a time
- The sequences of steps is START(where user gives an input), PLAN (that can be multiple times), and finally OUTPUT (which is going to be displayed to the user)
- Avoid using quotation marks inside the content field unless absolutely necessary. If quotes are required, escape them properly to produce valid JSON.

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

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

user_query = input("👉 : ")
message_history.append({
    "role": "user",
    "content": user_query
})

print("\n\n")

while True:
    response = client.chat.completions.create(
        model="gemini-3.5-flash",
        response_format={
            "type": "json_object"
        },
        messages=message_history
    )


    raw_result = (response.choices[0].message.content)      # gives a JSON string

    message_history.append({
        "role": "assistant",
        "content": raw_result
    })

    #json.loads() parses the JSON string and converts it into a Python object.

    try:
        parsed_result = json.loads(raw_result)
    except json.JSONDecodeError:
        print(raw_result)
        raise

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
    
    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break

print("\n\n")