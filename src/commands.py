from profile import (
    set_name,
    set_favorite_game,
)


def process_command(question, profile):

    question = question.strip().lower()

    if question.startswith("my name is "):

        name = question[11:].strip().title()

        set_name(profile, name)

        return f"Nice to meet you, {name}! I'll remember that."

    if question.startswith("my favorite game is "):

        game = question[20:].strip().title()

        set_favorite_game(profile, game)

        return f"Awesome! I'll remember that your favorite game is {game}."

    if question == "what is my name?":

        if "name" in profile:
            return f"Your name is {profile['name']}."

        return "I don't know your name yet."

    if question == "what is my favorite game?":

        if "favorite_game" in profile:
            return f"Your favorite game is {profile['favorite_game']}."

        return "I don't know your favorite game yet."

    return None