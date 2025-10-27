from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-4o",
    input="what is dynamic programming?"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a assistant called Jarvis skilled like Grok, claude, and ChatGPT."},
        {"role": "user", "content": "Explain the theory of relativity in simple terms."}
    ]
)
    
print(response.output_text)
print(response.choices[0].message.content)


