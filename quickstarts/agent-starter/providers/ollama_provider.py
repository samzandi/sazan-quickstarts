from __future__ import annotations

import json
import os
from urllib import request


class OllamaProvider:
    """Local Ollama adapter using the HTTP API and no third-party client."""

    def __init__(self, model: str | None = None, base_url: str | None = None) -> None:
        self.model = model or os.getenv("SAZAN_MODEL", "llama3.2")
        self.base_url = (base_url or os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")).rstrip("/")

    def generate(self, prompt: str) -> str:
        payload = json.dumps(
            {"model": self.model, "prompt": prompt, "stream": False}
        ).encode("utf-8")
        req = request.Request(
            f"{self.base_url}/api/generate",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with request.urlopen(req, timeout=120) as response:
            body = json.loads(response.read().decode("utf-8"))
        text = str(body.get("response", "")).strip()
        if not text:
            raise RuntimeError("Ollama returned no text output.")
        return text
