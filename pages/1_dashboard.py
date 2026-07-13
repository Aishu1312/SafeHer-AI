import streamlit as st
import datetime
from styles.css import inject_custom_css
from utils.i18n import _

st.set_page_config(page_title=_("Dashboard") + " - SafeHer AI", page_icon="🏠", layout="wide")
inject_custom_css()

st.title(_("Welcome to SafeHer AI"))
st.markdown(f"### {_('Hello')}, <span class='gradient-text'>{st.session_state.user['username']}</span> 👋", unsafe_allow_html=True)
st.caption(_("Your personalized safety dashboard"))

st.markdown("---")

# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(_("Safety Status"), "✅ " + _("Safe"), delta=_("All Clear"))
with col2:
    st.metric(_("Emergency Contacts"), f"{len(st.session_state.user['emergency_contacts'])}")
with col3:
    st.metric(_("Alerts This Week"), "0", delta=_("Normal"))
with col4:
    st.metric(_("Risk Score"), _("Low") + " (12%)", delta="-2%")

st.markdown("---")

# Quick Actions
st.subheader(f"🚀 {_('Quick Actions')}")
qc1, qc2, qc3, qc4 = st.columns(4)
with qc1:
    if st.button(f"🚨 {_('TRIGGER SOS')}", type="primary", use_container_width=True):
        st.session_state.sos_active = True
        st.switch_page("pages/2_sos.py")
with qc2:
    if st.button(f"📍 {_('Share Location')}", use_container_width=True):
        st.switch_page("pages/3_location.py")
with qc3:
    if st.button(f"🏥 {_('Find Help Centers')}", use_container_width=True):
        st.switch_page("pages/5_help_centers.py")
with qc4:
    if st.button(f"📞 {_('Fake Call')}", use_container_width=True):
        st.switch_page("pages/4_fake_call.py")

st.markdown("---")

# Custom Cards for Dashboard layout
c1, c2 = st.columns([2, 1])

with c1:
    st.markdown(f"""
        <div class="glass-card">
            <h3>🛡️ {_('About SafeHer AI')}</h3>
            <p>{_('We are dedicated to providing a safer environment through real-time tracking, AI risk detection, and seamless emergency contact integration.')}</p>
            <p>{_('Ensure your emergency contacts are up to date and your location permissions are enabled for the best experience.')}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="glass-card">
            <h3>📝 {_('Safety Tips of the Day')}</h3>
            <ul>
                <li>{_('Always share your live location with a trusted contact when traveling late.')}</li>
                <li>{_('Keep the SOS shortcut easily accessible on your home screen.')}</li>
                <li>{_('Stay aware of your surroundings and avoid isolated areas at night.')}</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="glass-card">
            <h3>🌤️ {_('Local Weather')}</h3>
            <h1>28°C</h1>
            <p>{_('Clear Sky')}<br>{_('Visibility')}: {_('Good for travel.')}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="glass-card">
            <h3>👤 {_('Profile Setup')}</h3>
            <p>{_('Your profile is <strong>80%</strong> complete.')}</p>
            <progress value="80" max="100" style="width:100%;"></progress>
            <p style="font-size:12px; color:#aaa; margin-top:5px;">{_('Add more emergency contacts to reach 100%.')}</p>
        </div>
    """, unsafe_allow_html=True)
