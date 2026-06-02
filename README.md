# 🤖 AI Chatbot

A conversational AI chatbot built with **Streamlit** and **OpenRouter**, supporting multiple LLM providers and live web search.

## Features

- 🧠 **Multi-model support** — Switch between GPT-4o, Claude, Gemini, Llama, Mistral and more
- 🌐 **Live web search** — Powered by Perplexity Sonar models with cited sources
- ⚡ **Streaming responses** — Tokens stream in real-time for a responsive feel
- 💬 **Conversation history** — Full multi-turn context sent on every request
- 🎛️ **Configurable** — Max tokens slider, model selector, clear chat button

## Demo

![Chatbot Screenshot](https://github.com/Balact07/AI-ChatBot/raw/main/screenshot.png)

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Balact07/AI-ChatBot.git
cd AI-ChatBot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

```bash
cp .env.example .env
```

Open `.env` and paste your [OpenRouter API key](https://openrouter.ai/keys):

```
OPENROUTER_API_KEY=sk-or-v1-...
```

### 4. Run the app

```bash
streamlit run chatbot_app.py
```

Open **http://localhost:8501** in your browser.

## Usage

| Feature | How to use |
|---|---|
| Switch model | Select from the **Model** dropdown in the sidebar |
| Web search | Toggle **🌐 Web Search** — automatically uses Perplexity Sonar |
| Adjust response length | Use the **Max tokens** slider |
| Clear conversation | Click **🗑️ Clear Chat** |

## Supported Models

**Chat models** (via OpenRouter):
- `openai/gpt-4o`, `openai/gpt-4o-mini`, `openai/o3-mini`
- `anthropic/claude-sonnet-4-5`, `anthropic/claude-opus-4-5`
- `google/gemini-2.5-pro`, `google/gemini-2.5-flash`
- `meta-llama/llama-3.3-70b-instruct`
- `mistralai/mistral-large`

**Web search models** (Perplexity):
- `perplexity/sonar`
- `perplexity/sonar-pro`
- `perplexity/sonar-reasoning`

## Tech Stack

- [Streamlit](https://streamlit.io/) — UI framework
- [OpenRouter](https://openrouter.ai/) — Unified LLM API gateway
- [OpenAI Python SDK](https://github.com/openai/openai-python) — API client
- [python-dotenv](https://github.com/theskumar/python-dotenv) — Environment variable management
