import unittest

from agent import FALLBACK, handle
from models import DocumentAction, DocumentRequest
from store import DOCUMENTS


class DocumentAgentTests(unittest.TestCase):
    def test_summary_is_grounded_and_cited(self):
        response = handle(DocumentRequest("welcome", DocumentAction.SUMMARIZE))
        self.assertTrue(response.grounded)
        self.assertEqual(response.source_id, "doc-welcome-001")
        self.assertIn("Sazan Quickstarts", response.answer)

    def test_known_fact_is_answered_from_document(self):
        response = handle(
            DocumentRequest("policy", DocumentAction.ANSWER, "Does it run shell commands?")
        )
        self.assertTrue(response.grounded)
        self.assertEqual(response.source_id, "doc-policy-001")
        self.assertIn("shell commands", response.answer)

    def test_unknown_fact_falls_back(self):
        response = handle(
            DocumentRequest("welcome", DocumentAction.ANSWER, "What is the refund policy?")
        )
        self.assertFalse(response.grounded)
        self.assertEqual(response.answer, FALLBACK)
        self.assertEqual(response.reason, "not_in_document")

    def test_unknown_document_is_rejected(self):
        response = handle(DocumentRequest("missing", DocumentAction.SUMMARIZE))
        self.assertFalse(response.grounded)
        self.assertEqual(response.reason, "unknown_document")

    def test_store_is_unchanged_after_requests(self):
        before = DOCUMENTS["policy"].text
        handle(DocumentRequest("policy", DocumentAction.SUMMARIZE))
        handle(DocumentRequest("policy", DocumentAction.ANSWER, "shell commands"))
        self.assertEqual(DOCUMENTS["policy"].text, before)


if __name__ == "__main__":
    unittest.main()
