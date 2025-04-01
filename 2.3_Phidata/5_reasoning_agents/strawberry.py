import asyncio

from phi.agent import Agent
from phi.cli.console import console
from utils.llm_environment import client

task = "How many 'r' are in the word 'strawberry'?"

regular_agent = Agent(model=client, markdown=True)
reasoning_agent = Agent(model=client, reasoning=True, markdown=True, structured_outputs=True)


async def main():
    console.rule("[bold blue]Counting 'r's in 'strawberry'[/bold blue]")

    console.rule("[bold green]Regular Agent[/bold green]")
    await regular_agent.aprint_response(task, stream=True)
    console.rule("[bold yellow]Reasoning Agent[/bold yellow]")
    await reasoning_agent.aprint_response(task, stream=True, show_full_reasoning=True)


asyncio.run(main())
