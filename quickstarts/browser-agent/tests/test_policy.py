import unittest

from policy import NavigationPolicy


class NavigationPolicyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = NavigationPolicy(frozenset({"example.com"}))

    def test_allows_explicit_host(self):
        self.assertEqual(
            self.policy.validate("https://example.com/docs"),
            "https://example.com/docs",
        )

    def test_blocks_disallowed_host(self):
        with self.assertRaises(ValueError):
            self.policy.validate("https://example.org")

    def test_blocks_localhost(self):
        with self.assertRaises(ValueError):
            self.policy.validate("http://localhost:8000")

    def test_blocks_private_ip(self):
        with self.assertRaises(ValueError):
            self.policy.validate("http://127.0.0.1")

    def test_blocks_non_http_scheme(self):
        with self.assertRaises(ValueError):
            self.policy.validate("file:///etc/passwd")


if __name__ == "__main__":
    unittest.main()
