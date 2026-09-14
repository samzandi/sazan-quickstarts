import unittest

from agent import Agent
from providers.mock import MockProvider


class AgentTests(unittest.TestCase):
    def test_mock_round_trip(self):
        agent = Agent(MockProvider())
        result = agent.run("hello")
        self.assertIsInstance(result, str)
        self.assertTrue(result.strip())


if __name__ == "__main__":
    unittest.main()
