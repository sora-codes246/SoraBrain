from commands import process_command
from planner import choose_tool
from tools.manager import execute_tool


def route(question, profile):

    response = process_command(question, profile)

    if response:
        return {
            "type": "command",
            "response": response,
        }

    plan = choose_tool(question)

    if plan["tool"] != "AI":

        response = execute_tool(question)

        if response:
            return {
                "type": "tool",
                "tool": response,
            }

    return {
        "type": "ai",
    }