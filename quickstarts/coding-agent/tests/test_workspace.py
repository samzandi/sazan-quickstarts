from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agent import CodingAgent
from workspace import SafeWorkspace


class WorkspaceTests(unittest.TestCase):
    def test_preview_does_not_modify_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "demo.py"
            target.write_text("print('old')\n", encoding="utf-8")
            agent = CodingAgent(SafeWorkspace(root))

            preview = agent.preview("demo.py", "print('new')\n")

            self.assertIn("-print('old')", preview.output)
            self.assertIn("+print('new')", preview.output)
            self.assertEqual(target.read_text(encoding="utf-8"), "print('old')\n")

    def test_read_and_list(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "a.txt").write_text("hello", encoding="utf-8")
            agent = CodingAgent(SafeWorkspace(root))

            self.assertIn("a.txt", agent.inspect().output)
            self.assertEqual(agent.read("a.txt").output, "hello")


if __name__ == "__main__":
    unittest.main()
