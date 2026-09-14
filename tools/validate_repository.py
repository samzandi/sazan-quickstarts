from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
QUICKSTARTS = ROOT / "quickstarts"
WORKFLOWS = ROOT / ".github" / "workflows"

EXPECTED = (
    "agent-starter",
    "browser-agent",
    "business-agent",
    "coding-agent",
    "computer-agent",
    "customer-support-agent",
    "document-agent",
    "email-agent",
    "mcp-starter",
    "research-agent",
    "reviva-agent",
)

LEGACY_WORKFLOWS = (
    "test-agent-starter.yml",
    "test-mcp-starter.yml",
)


def validate() -> list[str]:
    errors: list[str] = []
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    quickstarts_readme = (QUICKSTARTS / "README.md").read_text(encoding="utf-8")

    actual = sorted(
        path.name for path in QUICKSTARTS.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )

    if actual != sorted(EXPECTED):
        errors.append(f"quickstart set mismatch: expected={sorted(EXPECTED)} actual={actual}")

    for name in EXPECTED:
        directory = QUICKSTARTS / name
        if not (directory / "README.md").is_file():
            errors.append(f"{name}: missing README.md")
        if not (directory / "tests").is_dir():
            errors.append(f"{name}: missing tests directory")
        if f"`{name}`" not in root_readme:
            errors.append(f"{name}: missing from root README index")
        if f"`{name}`" not in quickstarts_readme:
            errors.append(f"{name}: missing from quickstarts/README.md index")
        if not (WORKFLOWS / f"{name}.yml").is_file():
            errors.append(f"{name}: missing canonical workflow {name}.yml")

    for legacy in LEGACY_WORKFLOWS:
        if (WORKFLOWS / legacy).exists():
            errors.append(f"legacy duplicate workflow still present: {legacy}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Repository validation passed for {len(EXPECTED)} quickstarts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
