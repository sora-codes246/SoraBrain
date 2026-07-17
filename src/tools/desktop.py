import subprocess

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def open_program(program, path=None):
    try:
        if path:
            subprocess.Popen(path)
        else:
            subprocess.Popen(program)

        return f"✅ Opening {program.title()}..."

    except Exception as e:
        return f"❌ Error opening {program}: {e}"


def run_desktop_command(question):

    question = question.lower()


    OPEN_WORDS = [
        "open",
        "launch",
        "start",
        "run",
    ]

    if any(word in question for word in OPEN_WORDS):

      

        if "chrome" in question:
            return open_program("Google Chrome", CHROME_PATH)

        if "calculator" in question:
            return open_program("Calculator", "calc")

        if "notepad" in question:
            return open_program("Notepad", "notepad")

        if "paint" in question:
            return open_program("Paint", "mspaint")

        if "powershell" in question:
            return open_program("PowerShell", "powershell")

        if "cmd" in question:
            return open_program("Command Prompt", "cmd")

        if "explorer" in question:
            return open_program("File Explorer", "explorer")

  

    return None