from groq import Groq
from typing import List
import os
GROQ_APIKEY = os.getenv("GROQ_APIKEY")

# Take out model name here into a variable
def call_groq(messages: List[str]):
    client = Groq(api_key=os.environ.get("GROQ_APIKEY"),)
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content