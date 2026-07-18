import webbrowser


def run_web_command(question):
    """
    Opens a Google search in the user's browser.
    """

    question = question.strip()

    lower = question.lower()

    if lower.startswith("search "):

        query = question[7:].strip()

        if not query:
            return "❌ Please enter something to search."

        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

        webbrowser.open(url)

        return f" Searching Google for '{query}'..."

    return None