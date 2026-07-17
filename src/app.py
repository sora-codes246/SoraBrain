from brain import ask_ai
from memory import load_memory, save_memory
from profile import load_profile, save_profile
from commands import process_command
from config import WELCOME_MESSAGE, EXIT_COMMANDS
from router import route


def greet(profile):
    print("=" * 40)
    print(" SoraBrain: Hello! I'm your personal AI assistant.")

    if profile.get("name"):
        print(f" Welcome back, {profile['name']}!")
    else:
        print(WELCOME_MESSAGE)

    print("=" * 40)
    print("Type 'exit' to quit.\n")


def main():
    # Load saved data
    profile = load_profile()
    messages = load_memory()

    # Show welcome message
    greet(profile)

    while True:
        question = input("You: ")

        decision = route(question, profile)

        if decision["type"] == "command":

            print()

            print(" SoraBrain:", decision["response"])

            print()

            continue

        # Check for built-in commands first
        response = process_command(question, profile)

        if response:
            print()

            print(" SoraBrain:", response)

            print()

            continue

        # Exit command
        if question.lower() in EXIT_COMMANDS:
            save_memory(messages)
            save_profile(profile)

            print("\nI'll be waiting for your arrival!")
            break

        # Save user message
        messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        # Ask the AI
        answer = ask_ai(messages)

        # Save AI response
        messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        # Save conversation
        save_memory(messages)

        print()
        print(" SoraBrain:", answer)
        print()


if __name__ == "__main__":
    main()