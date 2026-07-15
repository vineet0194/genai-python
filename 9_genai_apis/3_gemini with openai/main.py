import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# you can manually pass in api key and base url as such:
# using this, we are using openai library but using gemini's key/url
# this will redirect calls to gemini (but using openai library)
client = OpenAI(
    api_key=os.getenv('GEMINI_API_KEY'),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Google's OpenAI-compatible endpoint does not support the OpenAI Responses API as of now
# instead of the new Responses API, use  the older Chat Completions API => it is supported 

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "user",
            "content": "Hey there gemini!"
        }
    ]
)

print(response.choices[0].message.content)