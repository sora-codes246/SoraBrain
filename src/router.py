from commands import process_command
from tools.manager import execute_tool


def route(question, profile):
    """
    Decide how SoraBrain should handle the user's message.
    """

    # 1. Check built-in commands first
    response = process_command(question, profile)

    if response:
        return {
            "type": "command",
            "response": response,
        }

    # 2. Check if a tool should handle the request
    tool = execute_tool(question)

    if tool:
        return {
            "type": "tool",
            "tool": tool,
        }

    # 3. Otherwise send it to the AI
    return {
        "type": "ai",
    }