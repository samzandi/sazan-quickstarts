from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agent import CodingAgent
from models import CodingAction, CodingActionType
from policy import CodingPolicy
from workspace import SafeWorkspace


class CodingPolicyTests(unittest.TestCase):
    def test_blocks_path_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            policy = CodingPolicy(Path(temp_dir))
            with self.assertRaises(ValueError):
                policy.validate(CodingAction(CodingActionType.READ_FILE, "../secret.txt"))

    def test_write_requires_explicit_approval(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            agent = CodingAgent(SafeWorkspace(Path(temp_dir)))
            with self.assertRaises(PermissionError):
                agent.apply("file.txt", "new content")

    def test_write_stays_inside_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            agent = CodingAgent(SafeWorkspace(root))
            result = agent.apply("nested/file.txt", "safe", approved=True)
            self.assertEqual(result.output, "written")
            self.assertEqual((root / "nested/file.txt").read_text(encoding="utf-8"), "safe")


if __name__ == "__main__":
    unittest.main()
