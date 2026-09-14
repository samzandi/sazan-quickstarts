import re

from sources import all_sources


STOPWORDS = {"the", "a", "an", "and", "or", "of", "to", "in", "on", "is", "are", "what", "how", "why"}


def _terms(text: str) -> set[str]:
    words = set(re.findall(r"[a-z0-9]+", text.casefold()))
    return words - STOPWORDS


def retrieve(question: str, limit: int = 2) -> list[tuple[str, dict[str, str], int]]:
    query_terms = _terms(question)
    ranked: list[tuple[str, dict[str, str], int]] = []
    for source_id, source in all_sources().items():
        source_terms = _terms(source["title"] + " " + source["text"])
        score = len(query_terms & source_terms)
        if score > 0:
            ranked.append((source_id, source, score))
    ranked.sort(key=lambda item: (-item[2], item[0]))
    return ranked[:limit]
