"""Run `pip install openai duckduckgo-search` to install dependencies."""

from phi.agent import Agent
from llm_environment import client
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    name="Web Agent",
    model=client,
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Whats happening in France?", stream=True)
