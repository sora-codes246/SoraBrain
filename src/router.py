from commands import process_command


def route(question, profile):

    response = process_command(question, profile)

    if response:

        return {
            "type": "command",
            "response": response,
        }

    return {
        "type": "AI",
    }