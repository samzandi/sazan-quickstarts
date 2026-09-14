from knowledge import lookup
from models import SupportRequest, SupportResponse
from policy import classify_intent, must_escalate


ESCALATION_TEXT = "This request needs a human support review."


def handle(request: SupportRequest) -> SupportResponse:
    intent = classify_intent(request.message)
    if must_escalate(intent):
        return SupportResponse(
            answer=ESCALATION_TEXT,
            source_id=None,
            escalated=True,
            reason=intent.value,
        )

    result = lookup(request.message)
    if result is None:
        return SupportResponse(
            answer=ESCALATION_TEXT,
            source_id=None,
            escalated=True,
            reason="unsupported",
        )

    answer, source_id = result
    return SupportResponse(
        answer=answer,
        source_id=source_id,
        escalated=False,
    )
