# Agent UI

> Note: Fork and clone this repository if needed

### Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

## OpenAI Agents

### Export your API keys

```shell
export OPENAI_API_KEY=***
export EXA_API_KEY=***
```

### Install libraries

```shell
pip install -U openai exa_py duckduckgo-search yfinance pypdf sqlalchemy 'fastapi[standard]' youtube-transcript-api phidata
```

### Authenticate with phidata.app

```
phi auth
```

### Connect OpenAI Agents to the Agent UI

```shell
python cookbook/playground/demo.py
```