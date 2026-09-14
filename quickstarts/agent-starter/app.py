from __future__ import annotations

from agent import Agent
from providers.factory import build_provider


def main() -> None:
    provider = build_provider()
    agent = Agent(provider)

    print("Sazan Agent Starter")
    print(f"Provider: {provider.__class__.__name__}")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            task = input("You> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break

        if task.lower() in {"exit", "quit"}:
            print("Bye.")
            break
        if not task:
            continue

        try:
            result = agent.run(task)
        except Exception as exc:
            print(f"Error> {exc}\n")
            continue

        print(f"Agent> {result}\n")


if __name__ == "__main__":
    main()
