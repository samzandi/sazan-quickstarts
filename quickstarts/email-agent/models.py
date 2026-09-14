from dataclasses import dataclass
from enum import Enum


class MailIntent(str, Enum):
    ROUTINE = "routine"
    URGENT = "urgent"
    SENSITIVE = "sensitive"
    UNSUPPORTED = "unsupported"


@dataclass(frozen=True)
class EmailMessage:
    message_id: str
    sender: str
    subject: str
    body: str


@dataclass(frozen=True)
class DraftReply:
    message_id: str
    body: str
    intent: MailIntent
    requires_approval: bool = True
    escalated: bool = False
    reason: str | None = None
