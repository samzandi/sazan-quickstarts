import unittest

from agent import draft_reply, simulate_send
from mailbox import get_message
from models import EmailMessage, MailIntent
from policy import classify


class EmailAgentTests(unittest.TestCase):
    def test_routine_message_gets_draft(self):
        message = get_message("m-001")
        self.assertIsNotNone(message)
        draft = draft_reply(message)
        self.assertEqual(draft.intent, MailIntent.ROUTINE)
        self.assertFalse(draft.escalated)
        self.assertTrue(draft.requires_approval)

    def test_sensitive_payment_escalates(self):
        message = get_message("m-002")
        self.assertIsNotNone(message)
        draft = draft_reply(message)
        self.assertTrue(draft.escalated)
        self.assertEqual(draft.intent, MailIntent.SENSITIVE)

    def test_send_requires_explicit_approval(self):
        message = get_message("m-001")
        draft = draft_reply(message)
        with self.assertRaises(PermissionError):
            simulate_send(draft, approved=False)
        self.assertEqual(simulate_send(draft, approved=True), "simulated-send:m-001")

    def test_unknown_message_is_unsupported(self):
        message = EmailMessage("m-x", "x@example.test", "Hello", "Tell me a joke")
        self.assertEqual(classify(message), MailIntent.UNSUPPORTED)
        self.assertTrue(draft_reply(message).escalated)


if __name__ == "__main__":
    unittest.main()
