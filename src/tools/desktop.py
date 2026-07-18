import subprocess


CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def open_program(name, command):
    try:
        subprocess.Popen(command)
        return f"✅ Opening {name}..."
    except Exception as e:
        return f"❌ Error opening {name}: {e}"


def run_desktop_command(question):

    question = question.lower()

    # -------------------------
    # Chrome
    # -------------------------
    if "chrome" in question:
        return open_program("Google Chrome", CHROME_PATH)

    # -------------------------
    # Calculator
    # -------------------------
    if any(word in question for word in [
        "calculator",
        "calc",
        "calculate",
        "calculation",
    ]):
        return open_program("Calculator", "calc")

    # -------------------------
    # Notepad
    # -------------------------
    if any(word in question for word in [
        "notepad",
        "notes",
        "text editor",
    ]):
        return open_program("Notepad", "notepad")

    # -------------------------
    # Paint
    # -------------------------
    if "paint" in question:
        return open_program("Paint", "mspaint")

    # -------------------------
    # PowerShell
    # -------------------------
    if "powershell" in question:
        return open_program("PowerShell", "powershell")

    # -------------------------
    # Command Prompt
    # -------------------------
    if any(word in question for word in [
        "cmd",
        "command prompt",
        "terminal",
    ]):
        return open_program("Command Prompt", "cmd")

    # -------------------------
    # File Explorer
    # -------------------------
    if any(word in question for word in [
        "explorer",
        "file explorer",
        "files",
    ]):
        return open_program("File Explorer", "explorer")

    return None