import json
from pathlib import Path


PROFILE_FILE = Path("data/profile.json")


def load_profile():
    if PROFILE_FILE.exists():
        with open(PROFILE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return {}


def save_profile(profile):
    with open(PROFILE_FILE, "w", encoding="utf-8") as file:
        json.dump(profile, file, indent=4)

def set_name(profile, name):
    profile["name"] = name
    save_profile(profile)


def set_favorite_game(profile, game):
    profile["favorite_game"] = game
    save_profile(profile)
