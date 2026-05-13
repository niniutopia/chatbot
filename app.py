from openai import OpenAI
import streamlit as st

st.title("OpenRouter Chat Clone")

# 1. MODIFICA IL CLIENT: Aggiungi il base_url di OpenRouter e la tua API Key di OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"], 
    # OpenRouter consiglia di passare questi header opzionali per le statistiche:
    # default_headers={
    #     "HTTP-Referer": "YOUR_SITE_URL", # Opzionale
    #     "X-Title": "YOUR_APP_NAME",      # Opzionale
    # }
)

# 2. MODIFICA IL MODELLO: Inserisci l'ID del modello di OpenRouter (es. anthropic/claude-3-haiku, google/gemini-flash, ecc.)
if "model" not in st.session_state:
    st.session_state["model"] = "meta-llama/llama-3-8b-instruct" # Inserisci qui il tuo modello!

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["model"], # <-- Assicurati che punti alla variabile corretta
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})