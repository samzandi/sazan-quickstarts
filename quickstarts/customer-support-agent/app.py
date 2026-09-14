from agent import handle
from models import SupportRequest


if __name__ == "__main__":
    samples = [
        "What are your support hours?",
        "I want a refund to my card",
        "Tell me something not in the knowledge base",
    ]
    for text in samples:
        response = handle(SupportRequest(message=text))
        print({
            "message": text,
            "answer": response.answer,
            "source_id": response.source_id,
            "escalated": response.escalated,
            "reason": response.reason,
        })
