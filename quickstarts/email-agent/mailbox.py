from models import EmailMessage


MOCK_MAILBOX = {
    "m-001": EmailMessage(
        message_id="m-001",
        sender="customer@example.test",
        subject="Opening hours",
        body="Can you tell me your support hours?",
    ),
    "m-002": EmailMessage(
        message_id="m-002",
        sender="billing@example.test",
        subject="Refund request",
        body="Please refund my card payment immediately.",
    ),
}


def get_message(message_id: str) -> EmailMessage | None:
    return MOCK_MAILBOX.get(message_id)
