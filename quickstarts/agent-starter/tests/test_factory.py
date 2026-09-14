from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from providers.factory import build_provider
from providers.mock import MockProvider


class ProviderFactoryTests(unittest.TestCase):
    def test_defaults_to_mock(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            provider = build_provider()
        self.assertIsInstance(provider, MockProvider)

    def test_rejects_unknown_provider(self) -> None:
        with patch.dict(os.environ, {"SAZAN_PROVIDER": "unknown"}, clear=True):
            with self.assertRaises(ValueError):
                build_provider()


if __name__ == "__main__":
    unittest.main()
