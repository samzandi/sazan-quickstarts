from __future__ import annotations

from agent import Agent
from providers.mock import MockProvider


def main() -> None:
    agent = Agent(MockProvider())
    print("Sazan Agent Starter")
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

        print(f"Agent> {agent.run(task)}\n")


if __name__ == "__main__":
    main()
