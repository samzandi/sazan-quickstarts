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

REQUIRED_RELEASE_DOCS = (
    "docs/RELEASE_CHECKLIST.md",
    "docs/PRE_RELEASE_READINESS.md",
    "docs/THIRD_PARTY_LICENSES.md",
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

    for relative in REQUIRED_RELEASE_DOCS:
        if not (ROOT / relative).is_file():
            errors.append(f"missing release-readiness document: {relative}")

    third_party = ROOT / "docs" / "THIRD_PARTY_LICENSES.md"
    if third_party.is_file():
        third_party_text = third_party.read_text(encoding="utf-8").lower()
        for dependency in ("openai", "anthropic", "playwright", "mcp[cli]"):
            if dependency not in third_party_text:
                errors.append(f"third-party review missing direct dependency: {dependency}")
        if "transitive" not in third_party_text:
            errors.append("third-party review must address transitive dependencies")

    license_file = ROOT / "LICENSE"
    if not license_file.is_file():
        errors.append("missing repository LICENSE file")
    else:
        license_text = license_file.read_text(encoding="utf-8")
        if "Apache License" not in license_text or "Version 2.0" not in license_text:
            errors.append("repository LICENSE is not Apache-2.0")

    if "apache license, version 2.0" not in root_readme.lower():
        errors.append("root README must identify Apache-2.0 as the selected license")
    if "pre-release" not in root_readme.lower():
        errors.append("root README must explicitly state pre-release status")
    if "production-ready" not in root_readme.lower():
        errors.append("root README must explicitly address production-ready status")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Repository validation passed for {len(EXPECTED)} quickstarts, "
        f"{len(REQUIRED_RELEASE_DOCS)} release-readiness documents, Apache-2.0 licensing, "
        "and direct third-party dependency review."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
