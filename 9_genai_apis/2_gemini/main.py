from dotenv import load_dotenv
from google import genai

load_dotenv()

# by default, gemini client looks for "GOOGLE_API_KEY" or "GEMINI_API_KEY" env var in .env file
client = genai.Client()

response = client.interactions.create(
    model="gemini-3.5-flash",
    input="hi there gemini!"
)

print(response.output_text)