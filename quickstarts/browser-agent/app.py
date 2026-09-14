from __future__ import annotations

import os

from agent import BrowserAgent
from browser import SafeBrowser
from policy import NavigationPolicy


def _allowed_hosts() -> frozenset[str]:
    raw = os.getenv("SAZAN_BROWSER_ALLOWED_HOSTS", "example.com")
    hosts = {item.strip().lower().rstrip(".") for item in raw.split(",") if item.strip()}
    if not hosts:
        raise ValueError("SAZAN_BROWSER_ALLOWED_HOSTS must contain at least one host.")
    return frozenset(hosts)


def main() -> None:
    policy = NavigationPolicy(allowed_hosts=_allowed_hosts())
    with SafeBrowser(policy) as browser:
        agent = BrowserAgent(browser)
        url = input("URL> ").strip()
        snapshot = agent.open(url)
        print(f"Title: {snapshot.title}")
        print(f"URL: {snapshot.url}")
        print("\nText preview:\n")
        print(snapshot.text)


if __name__ == "__main__":
    main()
