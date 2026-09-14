import unittest

from agent import handle
from models import SupportRequest
from policy import SupportIntent, classify_intent


class CustomerSupportAgentTests(unittest.TestCase):
    def test_known_faq_uses_source(self):
        response = handle(SupportRequest("What are your support hours?"))
        self.assertFalse(response.escalated)
        self.assertEqual(response.source_id, "kb-hours-001")

    def test_sensitive_payment_escalates(self):
        response = handle(SupportRequest("Please refund my card payment"))
        self.assertTrue(response.escalated)
        self.assertEqual(response.reason, "payment")
        self.assertIsNone(response.source_id)

    def test_unknown_escalates(self):
        response = handle(SupportRequest("Can you recommend a laptop?"))
        self.assertTrue(response.escalated)
        self.assertEqual(response.reason, "unknown")

    def test_legal_is_detected(self):
        self.assertEqual(classify_intent("I need a lawyer"), SupportIntent.LEGAL)

    def test_medical_is_detected(self):
        self.assertEqual(classify_intent("I need medical advice"), SupportIntent.MEDICAL)


if __name__ == "__main__":
    unittest.main()
