from phi.model.openai import OpenAIChat

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAIChat(id="gpt-4o", api_key=api_key)



