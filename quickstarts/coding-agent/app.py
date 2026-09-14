from __future__ import annotations

import tempfile
from pathlib import Path

from agent import CodingAgent
from workspace import SafeWorkspace


def main() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        sample = root / "hello.py"
        sample.write_text("print('hello')\n", encoding="utf-8")

        agent = CodingAgent(SafeWorkspace(root))
        proposed = "print('hello from Sazan')\n"

        print("Files:")
        print(agent.inspect().output)
        print("\nPreview:")
        print(agent.preview("hello.py", proposed).output)
        print("Write not applied in demo; explicit approval is required.")


if __name__ == "__main__":
    main()
