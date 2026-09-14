import unittest

from browser import SafeBrowser
from policy import NavigationPolicy


class BrowserSmokeTests(unittest.TestCase):
    def test_chromium_can_render_and_snapshot(self):
        policy = NavigationPolicy(frozenset({"example.com"}))
        with SafeBrowser(policy) as browser:
            browser.page.set_content("<html><head><title>Sazan Test</title></head><body>Hello Browser</body></html>")
            snapshot = browser.snapshot()
            self.assertEqual(snapshot.title, "Sazan Test")
            self.assertIn("Hello Browser", snapshot.text)


if __name__ == "__main__":
    unittest.main()
