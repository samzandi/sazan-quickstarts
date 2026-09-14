SOURCES = {
    "src-ai-001": {
        "title": "Agent Safety Notes",
        "text": "Reliable agents should ground important claims in evidence and fail closed when evidence is missing.",
    },
    "src-ci-001": {
        "title": "Continuous Integration Notes",
        "text": "A test matrix can verify the same code on multiple supported Python versions before merge.",
    },
    "src-doc-001": {
        "title": "Research Workflow Notes",
        "text": "A compact research workflow retrieves relevant sources, records source identifiers, and separates supported findings from unknowns.",
    },
}


def all_sources() -> dict[str, dict[str, str]]:
    return {key: value.copy() for key, value in SOURCES.items()}
