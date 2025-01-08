from llm_library import call_groq

def test_call_groq():
    messages = [
        {
            "role": "system",
            "content": "Hello, how can I help you today?",
        },
        {
            "role": "user",
            "content": "I am looking for a recipe for a cake.",
        },
    ]
    response = call_groq(messages)
    print(response)

if __name__ == "__main__":
    test_call_groq()