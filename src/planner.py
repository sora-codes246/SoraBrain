import json
from ollama import chat
from config import MODEL_NAME


SYSTEM_PROMPT = """
You are the planner for SoraBrain.

Your job is NOT to answer the user.

Return ONLY valid JSON.

Available tools:

DESKTOP
FILES
WEB
AI

Examples:

User: Open Chrome

{
    "tool":"DESKTOP",
    "action":"OPEN_CHROME"
}

User: Open Calculator

{
    "tool":"DESKTOP",
    "action":"OPEN_CALCULATOR"
}

User: Create folder College

{
    "tool":"FILES",
    "action":"CREATE_FOLDER"
}

User: Search Python

{
    "tool":"WEB",
    "action":"SEARCH"
}

User: Explain recursion

{
    "tool":"AI",
    "action":"CHAT"
}
"""


def choose_tool(question):

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )

    try:
        return json.loads(response.message.content)

    except Exception:

        return {
            "tool": "AI",
            "action": "CHAT",
        }