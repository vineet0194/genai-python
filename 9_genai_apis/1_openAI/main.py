from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# by default, openAI client looks for "OPENAI_API_KEY" env var in .env file
client = OpenAI()

# old syntax ( Chat Completions API)
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Hi there gpt!"
        }
    ]
)

print(response.choices[0].message.content)


# new syntax ( Responses API )
response = client.responses.create(
    model="gpt-5.4-mini",
    input="Hi there gpt!"
)

print(response.output_text)