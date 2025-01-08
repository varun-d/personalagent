from typing import List, Union
from fastapi import FastAPI
import logging
from brain.worldcontext import getDateTimeContext
from brain.llm_library import call_groq

# Set up logging
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
LOG.info("API is starting up")

# Set up the messages list. Future, can this be a class?
messages = []

# Init the heavy lifting here. Chat sessions, system prompt, etc
with open ("personality.txt", "r") as file:
    personality = file.read()
    messages=[
        {
            "role": "system",
            "content": personality,
        }
            ]
    
# Create the FastAPI instance
app = FastAPI()

# Endpoints

# Root endpoint
@app.get("/")
def read_root():
    return {"Content": "This is running at the root of the server."}

@app.get("/testrun")
def testrun():
    return {"Test Endpoint": getDateTimeContext()}  

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/simple/{query}")
async def simple_resp(query: str):
    messages.append({"role": "user", "content": query + getDateTimeContext()})
    response = call_groq(messages)
    print(messages)
    return {"Response:": response}

# Main chat with llm as a post method
# @app.post("/chat")
# async def chat(query: str):
#     messages.append({"role": "user", "content": query})
#     response = call_groq(messages)
#     print(messages)
#     return {"Response:": response}