from phi.model.openai import OpenAIChat

from dotenv import load_dotenv
import os


class LLMEnvironment:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client =  OpenAIChat(id="gpt-4o", api_key=self.api_key)

    def get_client(self):
        return self.client


