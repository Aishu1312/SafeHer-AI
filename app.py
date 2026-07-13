import streamlit as st
from utils.session import init_session_state, login_user

st.set_page_config(page_title="SafeHer AI - Login", page_icon="🛡️", layout="centered")

# Initialize session state variables
init_session_state()

# CSS for login page
st.markdown("""
<style>
    .stTextInput > div > div > input {
        border-radius: 10px;
    }
    .stButton > button {
        border-radius: 10px;
        background-color: #E91E8C;
        color: white;
        border: none;
        width: 100%;
        padding: 10px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #7B2FBE;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align: center; color: #E91E8C;'>🛡️ SafeHer AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Your Intelligent Personal Safety Companion</p>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.subheader("Welcome Back")
        username = st.text_input("Username", value="Priya Sharma")
        password = st.text_input("Password", type="password", value="password123")
        
        if st.button("Login", key="login_btn"):
            if username and password:
                # In a real app, validate against a database
                login_user(
                    username=username,
                    email="priya.sharma@email.com",
                    mobile="+91-98765-43210",
                    blood_group="B+"
                )
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Please enter both username and password")
                
    with tab2:
        st.subheader("Create an Account")
        new_username = st.text_input("Full Name")
        new_email = st.text_input("Email")
        new_mobile = st.text_input("Mobile Number")
        new_bg = st.selectbox("Blood Group (Optional)", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Not specified"])
        new_password = st.text_input("Create Password", type="password")
        
        if st.button("Register", key="register_btn"):
            if new_username and new_email and new_mobile and new_password:
                login_user(
                    username=new_username,
                    email=new_email,
                    mobile=new_mobile,
                    blood_group=new_bg if new_bg != "Not specified" else ""
                )
                st.success("Registration successful!")
                st.rerun()
            else:
                st.error("Please fill in all required fields.")
else:
    # Use st.navigation for multipage layout when authenticated
    pages = {
        "Dashboard": [
            st.Page("pages/1_dashboard.py", title="Dashboard", icon="🏠"),
        ],
        "Safety Tools": [
            st.Page("pages/2_sos.py", title="SOS Emergency", icon="🚨"),
            st.Page("pages/3_location.py", title="Live Location", icon="📍"),
            st.Page("pages/4_fake_call.py", title="Fake Call", icon="📞"),
        ],
        "Resources": [
            st.Page("pages/5_help_centers.py", title="Help Centers", icon="🏥"),
            st.Page("pages/6_ai_assistant.py", title="AI Assistant", icon="🤖"),
        ],
        "Settings": [
            st.Page("pages/7_profile.py", title="Profile", icon="👤"),
        ]
    }
    
    pg = st.navigation(pages)
    
    # Global sidebar elements for authenticated users
    st.sidebar.title("🛡️ SafeHer AI")
    st.sidebar.markdown("---")
    st.sidebar.info(f"👤 **Logged in as:**\n{st.session_state.user['username']}")
    
    # Global SOS button in sidebar
    if st.sidebar.button("🚨 QUICK SOS", type="primary", use_container_width=True):
        st.session_state.sos_active = True
        # Let the SOS page handle the actual emergency action if it's open, 
        # but better yet we can switch to SOS page. Streamlit st.switch_page
        st.switch_page("pages/2_sos.py")
        
    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"):
        from utils.session import logout_user
        logout_user()
        st.rerun()
        
    pg.run()
