from dataclasses import dataclass


@dataclass(frozen=True)
class ResearchQuery:
    question: str


@dataclass(frozen=True)
class Finding:
    claim: str
    source_ids: tuple[str, ...]
    supported: bool
    reason: str | None = None


@dataclass(frozen=True)
class ResearchResponse:
    question: str
    findings: tuple[Finding, ...]
