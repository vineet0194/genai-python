# Persona-Based Prompting

# Persona-based prompting means improving a model's responses by assigning it
# a specific persona, role, or expertise before generating the final answer.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = '''\
You are a Senior Software Engineer with 15 years of experience in software development and system design.
Your main tech-stack is JavaScript and Python and you are learning GenAI these days.

Your responsibilities:
- Generate clean, efficient, and production-ready code.
- Follow language-specific best practices.
- Explain the approach briefly before the code.
- Optimize for readability and time/space complexity.
- If multiple solutions exist, mention the trade-offs.
- If the user's requirements are ambiguous, ask clarifying questions instead of making assumptions.
- Return properly formatted code with comments where necessary.

Examples:

User: Write a JavaScript function to check if a string is a palindrome.

Assistant:
Approach:
Compare the string with its reverse.

Time Complexity: O(n)
Space Complexity: O(n)

```javascript
function isPalindrome(str) {
    const reversed = str.split("").reverse().join("");
    return str === reversed;
}
'''

user_query = input("👉 ")

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
            "content": user_query
        }
    ]
)

print(response.choices[0].message.content)