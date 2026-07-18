from pathlib import Path
import shutil


def run_file_command(question):
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

    # ==========================
    # READ FILE
    # ==========================
    if lower.startswith("read file "):

        file_name = question[len("read file "):].strip()

        file = Path(file_name)

        if not file.exists():
            return "❌ File not found."

        content = file.read_text(encoding="utf-8")

        if not content:
            return "📄 File is empty."

        return f"\n📄 {file_name}\n\n{content}"

    # ==========================
    # RENAME FILE
    # ==========================
    if lower.startswith("rename file "):

        command = question[len("rename file "):]

        if " to " not in command:
            return "❌ Use: rename file old.txt to new.txt"

        old_name, new_name = command.split(" to ", 1)

        old_file = Path(old_name.strip())
        new_file = Path(new_name.strip())

        if not old_file.exists():
            return "❌ File not found."

        old_file.rename(new_file)

        return f"✅ Renamed '{old_name.strip()}' to '{new_name.strip()}'."

    # ==========================
    # DELETE FILE
    # ==========================
    if lower.startswith("delete file "):

        file_name = question[len("delete file "):].strip()

        file = Path(file_name)

        if not file.exists():
            return "❌ File not found."

        file.unlink()

        return f"🗑️ Deleted '{file_name}'."

    # ==========================
    # COPY FILE
    # ==========================
    if lower.startswith("copy file "):

        command = question[len("copy file "):]

        if " to " not in command:
            return "❌ Use: copy file notes.txt to backup.txt"

        source, destination = command.split(" to ", 1)

        source = Path(source.strip())
        destination = Path(destination.strip())

        if not source.exists():
            return "❌ Source file not found."

        shutil.copy2(source, destination)

        return f"✅ Copied '{source.name}' to '{destination}'."

    # ==========================
    # MOVE FILE
    # ==========================
    if lower.startswith("move file "):

        command = question[len("move file "):]

        if " to " not in command:
            return "❌ Use: move file notes.txt to folder/notes.txt"

        source, destination = command.split(" to ", 1)

        source = Path(source.strip())
        destination = Path(destination.strip())

        if not source.exists():
            return "❌ Source file not found."

        shutil.move(str(source), str(destination))

        return f"✅ Moved '{source.name}' to '{destination}'."

    return None