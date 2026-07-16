from ollama import chat

from config import MODEL_NAME


def ask_ai(messages):
    response = chat(
        model=MODEL_NAME,
        messages=messages,
    )

    return response.message.content