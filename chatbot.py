import os 
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import HuggingFaceEndpoint

# ---------------- MODEL ----------------
model = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="conversational",   # ✅ MUST FIX
    temperature=0.7
)

# ---------------- UI ----------------
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="💼"
)

st.title("💼 AI Career Advisor Chatbot")

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    system_prompt = """
    You are an expert career advisor AI.
    Ask about user's skills, interests, and goals.
    Give practical and actionable career advice.
    Be concise and helpful.
    """
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {}

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Tell me about your career goals...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Store simple memory
    if "python" in user_input.lower():
        st.session_state.user_profile["skill"] = "Python"
    if "data" in user_input.lower():
        st.session_state.user_profile["interest"] = "Data Science"

    # Inject memory
    context = f"User profile: {st.session_state.user_profile}"
    full_messages = st.session_state.messages + [
        {"role": "system", "content": context}
    ]

    # ✅ Call model
    response = model.invoke(full_messages)

    # ✅ Safe response handling
    if isinstance(response, dict):
        reply = response.get("generated_text", str(response))
    else:
        reply = str(response)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)

# ---------------- RESET ----------------
if st.button("🔄 Reset"):
    st.session_state.clear()
    st.rerun()