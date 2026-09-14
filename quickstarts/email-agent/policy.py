from models import EmailMessage, MailIntent


SENSITIVE_TERMS = (
    "password", "credential", "login", "2fa", "refund", "payment", "card",
    "bank", "legal", "lawyer", "court", "medical", "doctor", "security incident",
)
URGENT_TERMS = ("urgent", "asap", "immediately", "today")
ROUTINE_TERMS = ("hours", "opening", "shipping", "appointment", "information")


def classify(message: EmailMessage) -> MailIntent:
    text = f"{message.subject} {message.body}".casefold()
    if any(term in text for term in SENSITIVE_TERMS):
        return MailIntent.SENSITIVE
    if any(term in text for term in URGENT_TERMS):
        return MailIntent.URGENT
    if any(term in text for term in ROUTINE_TERMS):
        return MailIntent.ROUTINE
    return MailIntent.UNSUPPORTED


def can_simulate_send(*, approved: bool, escalated: bool) -> bool:
    return approved and not escalated
