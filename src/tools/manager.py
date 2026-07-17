from tools.desktop import run_desktop_command
from tools.files import run_file_command


def execute_tool(question):
    """
    Executes tools in order.
    """

    response = run_desktop_command(question)

    if response:
        return response

    response = run_file_command(question)

    if response:
        return response

    return None