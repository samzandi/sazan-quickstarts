from __future__ import annotations

import ipaddress
from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass(frozen=True)
class NavigationPolicy:
    """Explicitly restrict which destinations a browser agent may visit."""

    allowed_hosts: frozenset[str]

    def validate(self, url: str) -> str:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            raise ValueError("Only http and https URLs are allowed.")
        if not parsed.hostname:
            raise ValueError("URL must include a hostname.")

        host = parsed.hostname.lower().rstrip(".")
        if host == "localhost" or host.endswith(".localhost"):
            raise ValueError("Localhost targets are blocked.")

        try:
            ip = ipaddress.ip_address(host)
        except ValueError:
            ip = None
        if ip and (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved):
            raise ValueError("Private, loopback, link-local, and reserved IP targets are blocked.")

        if host not in self.allowed_hosts:
            raise ValueError(f"Host {host!r} is not in the navigation allowlist.")

        return url
