from models import DraftReply, EmailMessage, MailIntent
from policy import classify, can_simulate_send


ESCALATION_TEXT = "This message needs human review before a reply is prepared."


def draft_reply(message: EmailMessage) -> DraftReply:
    intent = classify(message)
    if intent in {MailIntent.SENSITIVE, MailIntent.UNSUPPORTED}:
        return DraftReply(
            message_id=message.message_id,
            body=ESCALATION_TEXT,
            intent=intent,
            escalated=True,
            reason=intent.value,
        )
    if intent is MailIntent.URGENT:
        body = "Thanks for your message. A human support agent should review this urgent request promptly."
    else:
        body = "Thanks for your message. Our support hours are Monday to Friday, 09:00 to 17:00 local time."
    return DraftReply(message_id=message.message_id, body=body, intent=intent)


def simulate_send(draft: DraftReply, *, approved: bool) -> str:
    if not can_simulate_send(approved=approved, escalated=draft.escalated):
        raise PermissionError("Explicit approval is required and escalated drafts cannot be sent.")
    return f"simulated-send:{draft.message_id}"
