from models import DocumentAction, DocumentRequest, DocumentResponse
from store import get_document


FALLBACK = "The requested information is not present in the selected document."


def _sentences(text: str) -> list[str]:
    return [part.strip() for part in text.split(".") if part.strip()]


def _answer_from_document(text: str, query: str) -> str | None:
    terms = [term for term in query.casefold().replace("?", "").split() if len(term) >= 4]
    for sentence in _sentences(text):
        lowered = sentence.casefold()
        if terms and any(term in lowered for term in terms):
            return sentence + "."
    return None


def handle(request: DocumentRequest) -> DocumentResponse:
    document = get_document(request.document_id)
    if document is None:
        return DocumentResponse(
            document_id=request.document_id,
            answer="Unknown document ID.",
            grounded=False,
            reason="unknown_document",
        )

    if request.action == DocumentAction.METADATA:
        return DocumentResponse(
            document_id=document.document_id,
            answer=f"title={document.title}; characters={len(document.text)}",
            grounded=True,
            source_id=document.source_id,
        )

    if request.action == DocumentAction.SUMMARIZE:
        first_two = _sentences(document.text)[:2]
        return DocumentResponse(
            document_id=document.document_id,
            answer=". ".join(first_two) + ("." if first_two else ""),
            grounded=True,
            source_id=document.source_id,
        )

    if request.action == DocumentAction.ANSWER:
        if not request.query:
            return DocumentResponse(
                document_id=document.document_id,
                answer=FALLBACK,
                grounded=False,
                reason="missing_query",
            )
        answer = _answer_from_document(document.text, request.query)
        if answer is None:
            return DocumentResponse(
                document_id=document.document_id,
                answer=FALLBACK,
                grounded=False,
                source_id=document.source_id,
                reason="not_in_document",
            )
        return DocumentResponse(
            document_id=document.document_id,
            answer=answer,
            grounded=True,
            source_id=document.source_id,
        )

    raise ValueError(f"Unsupported action: {request.action}")
