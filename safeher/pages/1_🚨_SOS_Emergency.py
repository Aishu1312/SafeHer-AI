import streamlit as st
import time
import datetime
from safeher.utils.helpers import get_mock_contacts

st.set_page_config(page_title="SOS Emergency – SafeHer AI", page_icon="🚨", layout="wide")

st.sidebar.title("🛡 SafeHer AI")
st.sidebar.caption("Intelligent Women Safety System")
st.sidebar.markdown("---")
st.sidebar.info("👤 **Logged in as:** Priya Sharma\n\n📍 **Status:** Safe")

st.title("🚨 SOS Emergency")
st.caption("One tap to trigger emergency alerts to your trusted contacts")

st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Emergency Trigger")
    st.markdown(
        """
        <div style='text-align:center; padding: 20px;'>
            <p style='font-size:16px; color:#aaa;'>Press the button below in an emergency</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    sos_pressed = st.button(
        "🚨  EMERGENCY SOS",
        use_container_width=True,
        type="primary",
    )
    if sos_pressed:
        with st.spinner("Activating SOS..."):
            time.sleep(1)
        st.error(
            "🚨 **SOS ACTIVATED!**\n\n"
            "✅ Emergency SMS sent to 3 contacts\n"
            "✅ Live location shared\n"
            "✅ Evidence recording started\n"
            "✅ Nearest police station notified"
        )
        st.balloons()

    st.markdown("---")
    st.subheader("SMS Preview")
    now = datetime.datetime.now().strftime("%d %b %Y %I:%M %p")
    st.code(
        f"[SafeHer AI EMERGENCY]\n"
        f"Priya Sharma needs help!\n"
        f"Time: {now}\n"
        f"Location: https://maps.google.com/?q=28.6139,77.2090\n"
        f"Call her immediately or contact Police: 100",
        language=None,
    )

with col2:
    st.subheader("📋 Trusted Emergency Contacts")
    contacts = get_mock_contacts()

    for c in contacts:
        with st.container():
            cc1, cc2, cc3 = st.columns([2, 2, 1])
            with cc1:
                st.markdown(f"**{c['name']}** ({c['relation']})")
                st.caption(c["phone"])
            with cc2:
                st.markdown("🟢 Reachable")
            with cc3:
                if st.button("📞 Call", key=f"call_{c['name']}"):
                    st.info(f"Calling {c['name']}...")
            st.markdown("---")

    st.subheader("➕ Add Emergency Contact")
    with st.form("add_contact_form"):
        nc1, nc2, nc3 = st.columns(3)
        with nc1:
            new_name = st.text_input("Full Name")
        with nc2:
            new_phone = st.text_input("Phone Number")
        with nc3:
            new_relation = st.selectbox("Relation", ["Mother", "Father", "Sister", "Brother", "Friend", "Husband", "Other"])
        if st.form_submit_button("Add Contact", use_container_width=True):
            if new_name and new_phone:
                st.success(f"✅ {new_name} added as an emergency contact!")
            else:
                st.warning("Please fill in all fields.")

st.markdown("---")
st.subheader("⚙️ SOS Settings")
sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.toggle("Auto-call emergency contacts", value=True)
    st.toggle("Send SMS alerts", value=True)
with sc2:
    st.toggle("Share live location", value=True)
    st.toggle("Record audio evidence", value=True)
with sc3:
    st.toggle("Capture photos automatically", value=True)
    st.toggle("Alert nearest police station", value=False)
