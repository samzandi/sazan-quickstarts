from models import SupportIntent


SENSITIVE_TERMS = {
    SupportIntent.ACCOUNT: ("password", "login", "account", "credential", "2fa"),
    SupportIntent.PAYMENT: ("payment", "refund", "card", "charge", "bank"),
    SupportIntent.LEGAL: ("lawyer", "legal", "lawsuit", "court"),
    SupportIntent.MEDICAL: ("medical", "doctor", "diagnosis", "medicine"),
    SupportIntent.ABUSE_RISK: ("threat", "kill", "attack", "harm"),
}


def classify_intent(message: str) -> SupportIntent:
    text = message.casefold()
    for intent, terms in SENSITIVE_TERMS.items():
        if any(term in text for term in terms):
            return intent
    if any(term in text for term in ("hours", "opening", "shipping", "return policy", "support")):
        return SupportIntent.FAQ
    return SupportIntent.UNKNOWN


def must_escalate(intent: SupportIntent) -> bool:
    return intent in {
        SupportIntent.ACCOUNT,
        SupportIntent.PAYMENT,
        SupportIntent.LEGAL,
        SupportIntent.MEDICAL,
        SupportIntent.ABUSE_RISK,
        SupportIntent.UNKNOWN,
    }
