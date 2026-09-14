import unittest

from actions import ComputerAction
from policy import ActionPolicy


class ActionPolicyTests(unittest.TestCase):
    def setUp(self):
        self.policy = ActionPolicy()

    def test_allows_observe(self):
        self.policy.validate(ComputerAction.observe())

    def test_blocks_text_entry(self):
        with self.assertRaises(PermissionError):
            self.policy.validate(ComputerAction(type="type_text", text="secret"))

    def test_requires_pointer_coordinates(self):
        with self.assertRaises(ValueError):
            self.policy.validate(ComputerAction(type="click"))

    def test_rejects_negative_coordinates(self):
        with self.assertRaises(ValueError):
            self.policy.validate(ComputerAction(type="move_pointer", x=-1, y=10))


if __name__ == "__main__":
    unittest.main()
