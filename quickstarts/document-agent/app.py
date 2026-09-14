from agent import handle
from models import DocumentAction, DocumentRequest


if __name__ == "__main__":
    samples = [
        DocumentRequest("welcome", DocumentAction.SUMMARIZE),
        DocumentRequest("policy", DocumentAction.ANSWER, "Does it run shell commands?"),
        DocumentRequest("welcome", DocumentAction.ANSWER, "What is the refund policy?"),
    ]
    for request in samples:
        print(handle(request))
