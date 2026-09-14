from __future__ import annotations

from browser import PageSnapshot, SafeBrowser


class BrowserAgent:
    """Minimal browser-agent orchestration with intentionally narrow capabilities."""

    def __init__(self, browser: SafeBrowser) -> None:
        self.browser = browser

    def open(self, url: str) -> PageSnapshot:
        return self.browser.open(url)

    def read(self, max_chars: int = 4000) -> PageSnapshot:
        return self.browser.snapshot(max_chars=max_chars)

    def follow_link(self, accessible_name: str) -> PageSnapshot:
        return self.browser.follow_link(accessible_name)
