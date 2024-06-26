from pathlib import Path
from tempfile import TemporaryDirectory

from langchain.agents.agent_types import AgentType
from langchain.agents.initialize import initialize_agent, load_agent
from langchain_core.language_models import FakeListLLM
from langchain_core.tools import Tool


def test_mrkl_serialization() -> None:
    agent = initialize_agent(
        [
            Tool(
                name="Test tool",
                func=lambda x: x,
                description="Test description",
            )
        ],
        FakeListLLM(responses=[]),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    with TemporaryDirectory() as tempdir:
        file = Path(tempdir) / "agent.json"
        agent.save_agent(file)
        load_agent(file)
