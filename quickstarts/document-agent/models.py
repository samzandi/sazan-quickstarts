from dataclasses import dataclass
from enum import Enum


class DocumentAction(str, Enum):
    SUMMARIZE = "summarize"
    ANSWER = "answer"
    METADATA = "metadata"


@dataclass(frozen=True)
class DocumentRequest:
    document_id: str
    action: DocumentAction
    query: str | None = None


@dataclass(frozen=True)
class DocumentResponse:
    document_id: str
    answer: str
    grounded: bool
    source_id: str | None = None
    reason: str | None = None
