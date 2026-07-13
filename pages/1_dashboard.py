import streamlit as st
import datetime
from styles.css import inject_custom_css

st.set_page_config(page_title="Dashboard - SafeHer AI", page_icon="🏠", layout="wide")
inject_custom_css()

st.title("Welcome to SafeHer AI")
st.markdown(f"### Hello, <span class='gradient-text'>{st.session_state.user['username']}</span> 👋", unsafe_allow_html=True)
st.caption("Your personalized safety dashboard")

st.markdown("---")

# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Safety Status", "✅ Safe", delta="All Clear")
with col2:
    st.metric("Emergency Contacts", f"{len(st.session_state.user['emergency_contacts'])}")
with col3:
    st.metric("Alerts This Week", "0", delta="Normal")
with col4:
    st.metric("Risk Score", "Low (12%)", delta="-2%")

st.markdown("---")

# Quick Actions
st.subheader("🚀 Quick Actions")
qc1, qc2, qc3, qc4 = st.columns(4)
with qc1:
    if st.button("🚨 TRIGGER SOS", type="primary", use_container_width=True):
        st.session_state.sos_active = True
        st.switch_page("pages/2_sos.py")
with qc2:
    if st.button("📍 Share Location", use_container_width=True):
        st.switch_page("pages/3_location.py")
with qc3:
    if st.button("🏥 Find Help Centers", use_container_width=True):
        st.switch_page("pages/5_help_centers.py")
with qc4:
    if st.button("📞 Fake Call", use_container_width=True):
        st.switch_page("pages/4_fake_call.py")

st.markdown("---")

# Custom Cards for Dashboard layout
c1, c2 = st.columns([2, 1])

with c1:
    st.markdown("""
        <div class="glass-card">
            <h3>🛡️ About SafeHer AI</h3>
            <p>We are dedicated to providing a safer environment through real-time tracking, AI risk detection, and seamless emergency contact integration.</p>
            <p>Ensure your emergency contacts are up to date and your location permissions are enabled for the best experience.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <h3>📝 Safety Tips of the Day</h3>
            <ul>
                <li>Always share your live location with a trusted contact when traveling late.</li>
                <li>Keep the SOS shortcut easily accessible on your home screen.</li>
                <li>Stay aware of your surroundings and avoid isolated areas at night.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="glass-card">
            <h3>🌤️ Local Weather</h3>
            <h1>28°C</h1>
            <p>Clear Sky<br>Visibility: Good for travel.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <h3>👤 Profile Setup</h3>
            <p>Your profile is <strong>80%</strong> complete.</p>
            <progress value="80" max="100" style="width:100%;"></progress>
            <p style="font-size:12px; color:#aaa; margin-top:5px;">Add more emergency contacts to reach 100%.</p>
        </div>
    """, unsafe_allow_html=True)
