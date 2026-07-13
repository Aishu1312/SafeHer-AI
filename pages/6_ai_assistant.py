import streamlit as st
from config.settings import LANGUAGES
from styles.css import inject_custom_css
import google.generativeai as genai

st.set_page_config(page_title="AI Assistant - SafeHer AI", page_icon="🤖", layout="wide")
inject_custom_css()

st.title("🤖 AI Safety Assistant")
st.caption("Multilingual AI companion for safety advice, mental support, and emergency guidance")
st.markdown("---")

col_lang, col_warn = st.columns([1, 2])
with col_lang:
    selected_lang = st.selectbox("🌐 Select Language", list(LANGUAGES.values()))

# Configure Gemini
api_key = st.secrets.get("GEMINI_API_KEY", "")
if not api_key:
    st.error("⚠️ GEMINI_API_KEY not found in Streamlit secrets. Please add it to enable the AI Assistant.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro")

# Initialize Chat
if "ai_chat_session" not in st.session_state:
    st.session_state.ai_chat_session = model.start_chat(history=[])
    
if "ai_chat_messages" not in st.session_state:
    st.session_state.ai_chat_messages = []
    
    # Add initial greeting
    welcome_msg = f"Hello {st.session_state.user['username']}! I am your SafeHer AI Safety Assistant. How can I help you today? I can provide safety advice, legal rights info, or self-defense tips."
    st.session_state.ai_chat_messages.append({"role": "assistant", "content": welcome_msg})

st.markdown("<div class='glass-card' style='height: 500px; overflow-y: auto;'>", unsafe_allow_html=True)

# Display Chat Messages
for message in st.session_state.ai_chat_messages:
    if message["role"] == "user":
        st.markdown(f"""
        <div style='display: flex; justify-content: flex-end; margin-bottom: 10px;'>
            <div style='background: rgba(233, 30, 140, 0.2); padding: 10px 15px; border-radius: 15px 15px 0 15px; max-width: 70%;'>
                {message["content"]}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='display: flex; justify-content: flex-start; margin-bottom: 10px;'>
            <div style='background: rgba(255, 255, 255, 0.1); padding: 10px 15px; border-radius: 15px 15px 15px 0; max-width: 70%;'>
                🤖 <strong>AI Assistant:</strong><br>{message["content"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Chat Input
if prompt := st.chat_input("Type your question here..."):
    # Display user message
    st.session_state.ai_chat_messages.append({"role": "user", "content": prompt})
    st.rerun()

# Handle AI Response (outside rerun)
if st.session_state.ai_chat_messages and st.session_state.ai_chat_messages[-1]["role"] == "user":
    user_msg = st.session_state.ai_chat_messages[-1]["content"]
    
    # Context prompt
    system_instruction = f"""
    You are an AI Safety Assistant for a Women Safety Platform called SafeHer AI.
    The user's name is {st.session_state.user['username']}.
    Please reply strictly in {selected_lang}.
    Provide empathetic, accurate, and actionable advice related to women's safety, self-defense, legal rights, mental support, and emergency guidance.
    """
    
    full_prompt = f"System Instruction: {system_instruction}\n\nUser: {user_msg}"
    
    with st.spinner("Thinking..."):
        try:
            response = st.session_state.ai_chat_session.send_message(full_prompt)
            st.session_state.ai_chat_messages.append({"role": "assistant", "content": response.text})
            st.rerun()
        except Exception as e:
            st.error(f"Error communicating with AI: {e}")
