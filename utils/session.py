import streamlit as st

def init_session_state():
    """Initializes all required session state variables."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    
    if "user" not in st.session_state:
        st.session_state.user = {
            "username": "",
            "email": "",
            "mobile": "",
            "blood_group": "",
            "emergency_contacts": [],
            "location": {"lat": None, "lon": None, "address": ""}
        }
    
    if "ai_chat_history" not in st.session_state:
        st.session_state.ai_chat_history = []
        
    if "sos_active" not in st.session_state:
        st.session_state.sos_active = False
        
    if "language" not in st.session_state:
        st.session_state.language = "English"

def login_user(username, email, mobile, blood_group):
    """Logs in the user and populates session state."""
    st.session_state.user["username"] = username
    st.session_state.user["email"] = email
    st.session_state.user["mobile"] = mobile
    st.session_state.user["blood_group"] = blood_group
    st.session_state.authenticated = True

def logout_user():
    """Logs out the user and clears session state."""
    st.session_state.authenticated = False
    st.session_state.user = {
        "username": "",
        "email": "",
        "mobile": "",
        "blood_group": "",
        "emergency_contacts": [],
        "location": {"lat": None, "lon": None, "address": ""}
    }
