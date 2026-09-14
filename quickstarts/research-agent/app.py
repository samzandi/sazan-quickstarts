from agent import research, validate_citations
from models import ResearchQuery


if __name__ == "__main__":
    samples = [
        "How should agents handle missing evidence?",
        "How can a Python test matrix help before merge?",
        "What is the population of Mars?",
    ]
    for question in samples:
        response = research(ResearchQuery(question=question))
        print({
            "question": question,
            "valid_citations": validate_citations(response),
            "findings": [
                {
                    "claim": finding.claim,
                    "source_ids": finding.source_ids,
                    "supported": finding.supported,
                    "reason": finding.reason,
                }
                for finding in response.findings
            ],
        })
