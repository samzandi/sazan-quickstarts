import unittest

from agent import research, validate_citations
from models import ResearchQuery
from retrieval import retrieve


class ResearchAgentTests(unittest.TestCase):
    def test_retrieval_finds_relevant_source(self):
        matches = retrieve("Python test matrix before merge")
        self.assertTrue(matches)
        self.assertEqual(matches[0][0], "src-ci-001")

    def test_supported_findings_have_source_ids(self):
        response = research(ResearchQuery("missing evidence agents"))
        self.assertTrue(response.findings[0].supported)
        self.assertTrue(response.findings[0].source_ids)
        self.assertTrue(validate_citations(response))

    def test_unknown_question_refuses_claim(self):
        response = research(ResearchQuery("population of Mars"))
        self.assertFalse(response.findings[0].supported)
        self.assertEqual(response.findings[0].source_ids, ())
        self.assertEqual(response.findings[0].reason, "insufficient_evidence")

    def test_source_store_is_copy(self):
        from sources import all_sources
        sources = all_sources()
        sources["src-ai-001"]["text"] = "changed"
        fresh = all_sources()
        self.assertNotEqual(fresh["src-ai-001"]["text"], "changed")


if __name__ == "__main__":
    unittest.main()
