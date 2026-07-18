from tools.desktop import run_desktop_command
from tools.files import run_file_command
from tools.web import run_web_command


def execute_tool(question):

    response = run_desktop_command(question)
    if response:
        return response

    response = run_file_command(question)
    if response:
        return response

    response = run_web_command(question)
    if response:
        return response

    return None