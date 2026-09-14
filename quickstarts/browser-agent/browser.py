from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import urljoin

from playwright.sync_api import Browser, Page, sync_playwright

from policy import NavigationPolicy


@dataclass
class PageSnapshot:
    url: str
    title: str
    text: str


class SafeBrowser:
    """Small read-oriented browser wrapper guarded by NavigationPolicy."""

    def __init__(self, policy: NavigationPolicy, headless: bool = True) -> None:
        self.policy = policy
        self.headless = headless
        self._playwright = None
        self._browser: Browser | None = None
        self._page: Page | None = None

    def __enter__(self) -> "SafeBrowser":
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(headless=self.headless)
        context = self._browser.new_context()
        self._page = context.new_page()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if self._browser is not None:
            self._browser.close()
        if self._playwright is not None:
            self._playwright.stop()

    @property
    def page(self) -> Page:
        if self._page is None:
            raise RuntimeError("Browser session has not been started.")
        return self._page

    def open(self, url: str) -> PageSnapshot:
        self.policy.validate(url)
        self.page.goto(url, wait_until="domcontentloaded")
        self.policy.validate(self.page.url)
        return self.snapshot()

    def snapshot(self, max_chars: int = 4000) -> PageSnapshot:
        text = self.page.locator("body").inner_text()[:max_chars]
        return PageSnapshot(url=self.page.url, title=self.page.title(), text=text)

    def follow_link(self, accessible_name: str) -> PageSnapshot:
        link = self.page.get_by_role("link", name=accessible_name)
        href = link.get_attribute("href")
        if href is None:
            raise ValueError("Selected link has no href.")

        target = urljoin(self.page.url, href)
        self.policy.validate(target)
        link.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.policy.validate(self.page.url)
        return self.snapshot()
