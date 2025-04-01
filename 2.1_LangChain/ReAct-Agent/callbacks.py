from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentFinish, LLMResult
from typing import Any, Dict, List


class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> Any:
        print(f"****************Prompt to LLM was:****************\n{prompts[0]}")
        print("*****************Prompt to LLM was:****************")

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        print(f"*****************LLM response:****************\n{response.generations[0][0].text}")
        print("*****************LLM response:****************")
