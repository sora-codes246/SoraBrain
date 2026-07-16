MEMORY_KEYWORDS = [
    "my name is",
    "my favorite",
    "i like",
    "i love",
    "i hate",
    "i study",
    "my birthday is",
    "my goal is",
    "my dream is",
    "my favorite color is",
    "my favorite food is",
    "my favorite movie is",
    "my favorite book is",
    "my favorite song is",
    "my favorite sport is",
    "my favorite hobby is",
]


def should_remember(text):
    text = text.lower()

    for keyword in MEMORY_KEYWORDS:
        if keyword in text:
            return True

    return False