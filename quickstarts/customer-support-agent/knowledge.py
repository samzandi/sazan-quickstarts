KNOWLEDGE = {
    "hours": {
        "source_id": "kb-hours-001",
        "answer": "Support hours are Monday to Friday, 09:00 to 17:00 local time.",
    },
    "shipping": {
        "source_id": "kb-shipping-001",
        "answer": "Standard shipping usually takes 3 to 5 business days in this demo.",
    },
    "return policy": {
        "source_id": "kb-returns-001",
        "answer": "This demo knowledge base allows returns within 14 days if the item is unused.",
    },
}


def lookup(message: str) -> tuple[str, str] | None:
    text = message.casefold()
    for key, item in KNOWLEDGE.items():
        if key in text:
            return item["answer"], item["source_id"]
    return None
