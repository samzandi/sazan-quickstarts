from dataclasses import dataclass
from enum import Enum


class SupportIntent(str, Enum):
    FAQ = "faq"
    ACCOUNT = "account"
    PAYMENT = "payment"
    LEGAL = "legal"
    MEDICAL = "medical"
    ABUSE_RISK = "abuse_risk"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class SupportRequest:
    message: str


@dataclass(frozen=True)
class SupportResponse:
    answer: str
    source_id: str | None
    escalated: bool
    reason: str | None = None
