from agent import Agent
from providers.mock import MockProvider


def test_agent_returns_provider_output() -> None:
    agent = Agent(MockProvider())
    result = agent.run("Say hello")
    assert "Sazan mock response:" in result
    assert "Say hello" in result
