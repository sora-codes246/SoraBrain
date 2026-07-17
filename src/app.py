from brain import ask_ai
from memory import load_memory, save_memory
from profile import load_profile, save_profile
from config import WELCOME_MESSAGE, EXIT_COMMANDS
from router import route


def greet(profile):
    print("=" * 40)
    print(" SoraBrain")
    print("=" * 40)

    if profile.get("name"):
        print(f"Welcome back, {profile['name']}!")
    else:
        print(WELCOME_MESSAGE)

    print("=" * 40)
    print("Type 'exit' to quit.\n")


def main():

    profile = load_profile()
    messages = load_memory()

    greet(profile)

    while True:

        question = input("You: ")

        # Exit
        if question.lower() in EXIT_COMMANDS:
            save_memory(messages)
            save_profile(profile)

            print("\n👋 Goodbye!")
            break

        decision = route(question, profile)

        # COMMAND
        if decision["type"] == "command":

            print()
            print(" SoraBrain:", decision["response"])
            print()

            continue

        # TOOL
        if decision["type"] == "tool":

            print()
            print(" SoraBrain:", decision["tool"])
            print()

            continue

        # AI
        messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        answer = ask_ai(messages)

        messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        save_memory(messages)

        print()
        print(" SoraBrain:", answer)
        print()


if __name__ == "__main__":
    main()