from ollama import chat


def greet():
    print("=" * 40)
    print("🧠 Welcome to SoraBrain")
    print("=" * 40)
    print()


def main():
    greet()

    while True:
        question = input("You: ")

        if question.lower() in ["exit", "quit", "bye"]:
            print("\n👋 Goodbye, Sora!")
            break

        response = chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
        )

        print()
        print("🧠 SoraBrain:", response.message.content)
        print()


if __name__ == "__main__":
    main()