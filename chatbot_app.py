import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

SYSTEM_PROMPT = """You are a helpful, friendly, professional and knowledgeable AI assistant. \
You provide clear, accurate, and concise responses to help users with their questions and tasks."""

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 AI Chatbot")
st.caption(f"Powered by Bala")

with st.sidebar:
    st.header("Options")

    web_search = st.toggle("🌐 Web Search", value=False, help="Fetch live data from the internet")

    if web_search:
        model = st.selectbox(
            "Model",
            options=[
                "perplexity/sonar",
                "perplexity/sonar-pro",
                "perplexity/sonar-reasoning",
            ],
            help="Perplexity models are built for live web search",
        )
    else:
        model = st.selectbox(
            "Model",
            options=[
                "openai/gpt-4o",
                "openai/gpt-4o-mini",
                "openai/o3-mini",
                "anthropic/claude-opus-4-5",
                "anthropic/claude-sonnet-4-5",
                "google/gemini-2.5-pro",
                "google/gemini-2.5-flash",
                "meta-llama/llama-3.3-70b-instruct",
                "mistralai/mistral-large",
            ],
        )

    max_tokens = st.slider("Max tokens", min_value=256, max_value=8192, value=1024, step=256)

    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.caption(f"Messages in history: {len(st.session_state.messages)}")

client = OpenAI(api_key=OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("citations"):
            st.divider()
            st.caption("**Sources**")
            for i, url in enumerate(message["citations"], 1):
                st.caption(f"{i}. [{url}]({url})")

if prompt := st.chat_input("Message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # System prompt prepended to every request
    api_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + [
        {"role": msg["role"], "content": msg["content"]}
        for msg in st.session_state.messages
    ]

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        citations = []

        active_model = model

        if web_search:
            # Non-streaming — needed to access top-level citations field
            with st.spinner("🔍 Searching the web..."):
                response = client.chat.completions.create(
                    model=active_model,
                    messages=api_messages,
                    max_tokens=max_tokens,
                )
            full_response = response.choices[0].message.content or ""
            citations = (response.model_extra or {}).get("citations", [])
            placeholder.markdown(full_response)
        else:
            stream = client.chat.completions.create(
                model=active_model,
                messages=api_messages,
                max_tokens=max_tokens,
                stream=True,
            )
            for chunk in stream:
                text = chunk.choices[0].delta.content or ""
                full_response += text
                placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)

        if citations:
            st.divider()
            st.caption("**Sources**")
            for i, url in enumerate(citations, 1):
                st.caption(f"{i}. [{url}]({url})")

    st.session_state.messages.append({"role": "assistant", "content": full_response, "citations": citations})
