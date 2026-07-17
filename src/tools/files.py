from pathlib import Path


def run_file_command(question):
    """
    Handles simple file and folder operations.
    """

    question = question.strip()
    lower = question.lower()

    # ==========================
    # CREATE FOLDER
    # ==========================

    if lower.startswith("create folder "):

        folder_name = question[len("create folder "):].strip()

        if not folder_name:
            return "❌ Please provide a folder name."

        folder = Path(folder_name)

        if folder.exists():
            return f"📁 Folder '{folder_name}' already exists."

        folder.mkdir(parents=True)

        return f"✅ Folder '{folder_name}' created."

    # ==========================
    # CREATE FILE
    # ==========================

    if lower.startswith("create file "):

        file_name = question[len("create file "):].strip()

        if not file_name:
            return "❌ Please provide a file name."

        file = Path(file_name)

        if file.exists():
            return f"📄 File '{file_name}' already exists."

        file.touch()

        return f"✅ File '{file_name}' created."

    # ==========================
    # WRITE TO FILE
    # ==========================

    if lower.startswith("write "):

        if " to " not in question:
            return "❌ Use: write <text> to <filename>"

        text, file_name = question[6:].split(" to ", 1)

        file = Path(file_name.strip())

        file.write_text(text.strip(), encoding="utf-8")

        return f"✅ Written to '{file_name.strip()}'."

    return None