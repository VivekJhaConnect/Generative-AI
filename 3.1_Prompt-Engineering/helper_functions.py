import os

from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv
import csv
from langchain_openai import ChatOpenAI

# Get the OpenAI API key from the .env file
load_dotenv(dotenv_path="C:/Users/ADMIN/Documents/venv/.env", override=True)

client_name = "OPENAI"
model_name = "gpt-4o-mini" #"gpt-4o"

if client_name == "ANTHROPIC":
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
    llm = Anthropic(api_key=anthropic_api_key)
elif client_name == "CLAUDE_VERTEX":
    claude_api_key = os.getenv('CLAUDE_VERTEX_API_KEY')
    llm = Anthropic(api_key=claude_api_key)
elif client_name == "CLAUDE_3_5_SONNET":
    claude_api_key = os.getenv('CLAUDE_3_5_SONNET_API_KEY')
    llm = Anthropic(api_key=claude_api_key)
elif client_name == "AZIRE_OPENAI":
    azire_openai_api_key = os.getenv('AZIRE_OPENAI_API_KEY')
    llm = OpenAI(api_key=azire_openai_api_key)
elif client_name == "AZIRE_ANTHROPIC":
    azire_anthropic_api_key = os.getenv('AZIRE_ANTHROPIC_API_KEY')
    llm = Anthropic(api_key=azire_anthropic_api_key)
else:
    openai_api_key = os.getenv('OPENAI_API_KEY')
    llm = ChatOpenAI(api_key=openai_api_key)
    

def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then prints the response of the model.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion = llm.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        response = completion.choices[0].message.content
        print("_"*100)
        print(response)
        print("_"*100)
        print("\n")
    except TypeError as e:
        print("Error:", str(e))


def get_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then saves the response of the model as
    a string.
    """
    completion = llm.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response


def get_chat_completion(prompt, history):
    history_string = "\n\n".join(["\n".join(turn) for turn in history])
    prompt_with_history = f"{history_string}\n\n{prompt}"
    completion = llm.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt_with_history},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response
