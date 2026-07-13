import streamlit as st
from utils.session import init_session_state, login_user
from utils.i18n import _, LANGUAGE_CODES

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

# Language Selector (Available globally)
langs = list(LANGUAGE_CODES.keys())
current_lang_idx = langs.index(st.session_state.language) if st.session_state.language in langs else 0

if not st.session_state.authenticated:
    st.markdown(f"<h1 style='text-align: center; color: #E91E8C;'>🛡️ {_('SafeHer AI')}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>{_('Your Intelligent Personal Safety Companion')}</p>", unsafe_allow_html=True)
    
    st.selectbox(_("Select Language"), langs, index=current_lang_idx, key="lang_selector", on_change=lambda: st.session_state.update(language=st.session_state.lang_selector))
    
    tab1, tab2 = st.tabs([_("Login"), _("Register")])
    
    with tab1:
        st.subheader(_("Welcome Back"))
        username = st.text_input(_("Username"), value="Priya Sharma")
        password = st.text_input(_("Password"), type="password", value="password123")
        
        if st.button(_("Login"), key="login_btn"):
            if username and password:
                login_user(
                    username=username,
                    email="priya.sharma@email.com",
                    mobile="+91-98765-43210",
                    blood_group="B+"
                )
                st.success(_("Login successful!"))
                st.rerun()
            else:
                st.error(_("Please enter both username and password"))
                
    with tab2:
        st.subheader(_("Create an Account"))
        new_username = st.text_input(_("Full Name"))
        new_email = st.text_input(_("Email"))
        new_mobile = st.text_input(_("Mobile Number"))
        new_bg = st.selectbox(_("Blood Group (Optional)"), ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", _("Not specified")])
        new_password = st.text_input(_("Create Password"), type="password")
        
        if st.button(_("Register"), key="register_btn"):
            if new_username and new_email and new_mobile and new_password:
                login_user(
                    username=new_username,
                    email=new_email,
                    mobile=new_mobile,
                    blood_group=new_bg if new_bg != _("Not specified") else ""
                )
                st.success(_("Registration successful!"))
                st.rerun()
            else:
                st.error(_("Please fill in all required fields."))
else:
    # Use st.navigation for multipage layout when authenticated
    pages = {
        _("Dashboard"): [
            st.Page("pages/1_dashboard.py", title=_("Dashboard"), icon="🏠"),
        ],
        _("Safety Tools"): [
            st.Page("pages/2_sos.py", title=_("SOS Emergency"), icon="🚨"),
            st.Page("pages/3_location.py", title=_("Live Location"), icon="📍"),
            st.Page("pages/4_fake_call.py", title=_("Fake Call"), icon="📞"),
        ],
        _("Resources"): [
            st.Page("pages/5_help_centers.py", title=_("Help Centers"), icon="🏥"),
            st.Page("pages/6_ai_assistant.py", title=_("AI Assistant"), icon="🤖"),
        ],
        _("Settings"): [
            st.Page("pages/7_profile.py", title=_("Profile"), icon="👤"),
        ]
    }
    
    pg = st.navigation(pages)
    
    # Global sidebar elements for authenticated users
    st.sidebar.title(f"🛡️ {_('SafeHer AI')}")
    st.sidebar.selectbox(_("Select Language"), langs, index=current_lang_idx, key="lang_selector_auth", on_change=lambda: st.session_state.update(language=st.session_state.lang_selector_auth))
    st.sidebar.markdown("---")
    st.sidebar.info(f"👤 **{_('Logged in as')}:**\n{st.session_state.user['username']}")
    
    # Global SOS button in sidebar
    if st.sidebar.button(f"🚨 {_('QUICK SOS')}", type="primary", use_container_width=True):
        st.session_state.sos_active = True
        st.switch_page("pages/2_sos.py")
        
    st.sidebar.markdown("---")
    if st.sidebar.button(_("Logout")):
        from utils.session import logout_user
        logout_user()
        st.rerun()
        
    pg.run()
