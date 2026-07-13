import streamlit as st
from styles.css import inject_custom_css
from localization.manager import _
from services.ai_service import AIService

st.set_page_config(page_title=_("AI Assistant") + " - SafeHer AI", page_icon="🤖", layout="wide")
inject_custom_css()

st.title(f"🤖 {_('AI Safety Assistant')}")
st.caption(_("Multilingual AI companion for safety advice, mental support, and emergency guidance"))
st.markdown("---")

# Use global selected language
selected_lang = st.session_state.get('language', 'English')

# Initialize AI Service
@st.cache_resource
def get_ai_service():
    return AIService()

ai_service = get_ai_service()

# Graceful degradation if API key is missing
if not ai_service.is_available:
    st.markdown(f"""
    <div class="glass-card" style="border-left: 5px solid #FF9800; padding: 20px; margin-bottom: 20px;">
        <h3 style="color: #FF9800; margin-top: 0;">⚠️ {_('AI Assistant Unavailable')}</h3>
        <p>{_('The AI Assistant is temporarily unavailable. Please configure the API key to enable AI-powered assistance.')}</p>
        <p style="color: #aaa; font-size: 13px;">{_('Other features like SOS, Location Tracking, and Help Centers continue to work normally.')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander(_("Configure API Key")):
        st.markdown(_("Get your free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)"))
        user_key = st.text_input(_("Enter your Gemini API Key"), type="password")
        if st.button(_("Save API Key")):
            import os
            if user_key.strip():
                os.environ["GEMINI_API_KEY"] = user_key.strip()
                try:
                    with open(".env", "a") as f:
                        f.write(f"\nGEMINI_API_KEY={user_key.strip()}\n")
                except:
                    pass
                st.cache_resource.clear()
                st.rerun()
            else:
                st.error(_("Please enter a valid API key."))
    
    st.stop()

# Initialize Chat
if "ai_chat_session" not in st.session_state:
    st.session_state.ai_chat_session = ai_service.start_chat()
    
if "ai_chat_messages" not in st.session_state:
    st.session_state.ai_chat_messages = []
    
    # Add initial greeting
    welcome_msg = _("Hello") + f" {st.session_state.user['username']}! " + _("I am your SafeHer AI Safety Assistant. How can I help you today? I can provide safety advice, legal rights info, or self-defense tips.")
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
                🤖 <strong>{_('AI Assistant')}:</strong><br>{message["content"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Chat Input
if prompt := st.chat_input(_("Type your question here...")):
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
    
    with st.spinner(_("Thinking...")):
        try:
            response_text = ai_service.send_message(st.session_state.ai_chat_session, full_prompt)
            st.session_state.ai_chat_messages.append({"role": "assistant", "content": response_text})
            st.rerun()
        except Exception:
            # We catch the exception (logged by ai_service) and show a clean UI message
            st.error(_("The AI Assistant is currently experiencing high traffic or network issues. Please try again later."))
