"""Run `pip install yfinance` to install dependencies."""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from utils.llm_environment import client

finance_agent = Agent(
    name="Finance Agent",
    model=client,
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent.print_response("Share analyst recommendations for NVDA", stream=True)
