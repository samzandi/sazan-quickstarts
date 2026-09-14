from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    document_id: str
    title: str
    text: str
    source_id: str


DOCUMENTS = {
    "welcome": Document(
        document_id="welcome",
        title="Welcome Guide",
        text=(
            "Sazan Quickstarts is an educational repository for provider-neutral AI agent examples. "
            "Examples are intentionally constrained and are not production-ready. "
            "The repository uses an issue-driven workflow with tests and CI evidence before completion."
        ),
        source_id="doc-welcome-001",
    ),
    "policy": Document(
        document_id="policy",
        title="Demo Policy",
        text=(
            "This demo is read-only. It does not modify source documents, call external networks, "
            "run shell commands, handle secrets, or access arbitrary filesystem paths."
        ),
        source_id="doc-policy-001",
    ),
}


def get_document(document_id: str) -> Document | None:
    return DOCUMENTS.get(document_id)
