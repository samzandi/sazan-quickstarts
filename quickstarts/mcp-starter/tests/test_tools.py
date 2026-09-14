from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import add, health


class ToolTests(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_health(self) -> None:
        self.assertEqual(
            health(),
            {"status": "ok", "service": "sazan-mcp-starter"},
        )


if __name__ == "__main__":
    unittest.main()
