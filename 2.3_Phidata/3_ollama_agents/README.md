## Fully local Ollama Agents

### Pull llama3.1:8b

```shell
ollama pull llama3.1:8b
```

### Install libraries

```shell
pip install -U ollama duckduckgo-search yfinance pypdf sqlalchemy 'fastapi[standard]' phidata youtube-transcript-api
```

### Connect Ollama agents to the Agent UI

```shell
python cookbook/playground/ollama_agents.py
```

## Grok Agents

### Install libraries

```shell
pip install -U openai duckduckgo-search yfinance pypdf sqlalchemy 'fastapi[standard]' phidata youtube-transcript-api
```

### Connect Grok agents to the Agent UI

```shell
python cookbook/playground/grok_agents.py
```
