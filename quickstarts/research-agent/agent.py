from models import Finding, ResearchQuery, ResearchResponse
from retrieval import retrieve


UNSUPPORTED = "The bounded source set does not provide enough evidence for this claim."


def research(query: ResearchQuery) -> ResearchResponse:
    matches = retrieve(query.question)
    if not matches:
        return ResearchResponse(
            question=query.question,
            findings=(Finding(claim=UNSUPPORTED, source_ids=(), supported=False, reason="insufficient_evidence"),),
        )

    findings = tuple(
        Finding(
            claim=source["text"],
            source_ids=(source_id,),
            supported=True,
        )
        for source_id, source, _score in matches
    )
    return ResearchResponse(question=query.question, findings=findings)


def validate_citations(response: ResearchResponse) -> bool:
    return all((not finding.supported) or bool(finding.source_ids) for finding in response.findings)
