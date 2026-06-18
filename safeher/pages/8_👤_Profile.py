import streamlit as st
import datetime

st.set_page_config(page_title="Profile – SafeHer AI", page_icon="👤", layout="wide")

st.sidebar.title("🛡 SafeHer AI")
st.sidebar.caption("Intelligent Women Safety System")
st.sidebar.markdown("---")
st.sidebar.info("👤 **Logged in as:** Priya Sharma\n\n📍 **Status:** Safe")

st.title("👤 User Profile & Settings")
st.caption("Manage your account, contacts, and preferences")

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["👤 Profile", "🔔 Notifications", "🔒 Privacy & Security", "ℹ️ About App"])

with tab1:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(
            """
            <div style='text-align:center; padding:20px;'>
                <p style='font-size:72px; margin:0;'>👩</p>
                <p style='font-size:20px; font-weight:bold;'>Priya Sharma</p>
                <p style='color:#E91E8C;'>🛡 Premium Member</p>
                <p style='color:#aaa; font-size:13px;'>Member since Jan 2024</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button("📷 Change Profile Photo", use_container_width=True)

    with col2:
        st.subheader("Personal Information")
        with st.form("profile_form"):
            fc1, fc2 = st.columns(2)
            with fc1:
                st.text_input("Full Name", value="Priya Sharma")
                st.text_input("Email", value="priya.sharma@email.com")
                st.text_input("City", value="New Delhi")
            with fc2:
                st.text_input("Phone", value="+91-98765-43210")
                st.date_input("Date of Birth", value=datetime.date(1998, 5, 15))
                st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], index=2)
            st.text_area("Medical Notes (for emergency responders)", placeholder="e.g. No known allergies, takes blood pressure medication")
            if st.form_submit_button("💾 Save Changes", use_container_width=True):
                st.success("✅ Profile updated successfully!")

    st.markdown("---")
    st.subheader("📊 Your Safety Stats")
    sc1, sc2, sc3, sc4 = st.columns(4)
    with sc1:
        st.metric("Total Trips Tracked", "187")
    with sc2:
        st.metric("SOS Events", "2", delta="All Resolved")
    with sc3:
        st.metric("Safe Arrivals", "185")
    with sc4:
        st.metric("Risk Score (Avg)", "18%", delta="Low")

with tab2:
    st.subheader("🔔 Notification Preferences")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Push Notifications**")
        st.toggle("SOS Alerts", value=True)
        st.toggle("Location Sharing Updates", value=True)
        st.toggle("Route Deviation Warnings", value=True)
        st.toggle("Low Battery Warnings", value=True)
        st.toggle("Daily Safety Digest", value=False)
    with col2:
        st.markdown("**SMS Notifications**")
        st.toggle("SMS on SOS trigger", value=True)
        st.toggle("SMS when arriving safely", value=True)
        st.toggle("SMS for high risk detection", value=False)
        st.toggle("Weekly SMS report", value=False)

    st.markdown("---")
    st.subheader("⏰ Safe Check-In Intervals")
    checkin = st.select_slider(
        "Remind me to check in every",
        options=["15 min", "30 min", "1 hour", "2 hours", "4 hours", "Never"],
        value="1 hour",
    )
    st.caption(f"You'll receive a check-in reminder every **{checkin}** when tracking is active.")

with tab3:
    st.subheader("🔒 Security Settings")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Account Security**")
        st.toggle("Two-Factor Authentication", value=True)
        st.toggle("Biometric Login (Fingerprint/Face)", value=True)
        st.toggle("Auto-lock after 5 minutes", value=True)
        if st.button("🔑 Change Password"):
            st.info("A password reset link will be sent to your email.")
    with col2:
        st.markdown("**Data Privacy**")
        st.toggle("Store location history (30 days)", value=True)
        st.toggle("Allow anonymous analytics", value=False)
        st.toggle("Share data for AI improvement", value=False)
        if st.button("🗑️ Delete All My Data", type="secondary"):
            st.error("⚠️ This will permanently delete all your data. Please confirm via email.")

    st.markdown("---")
    st.subheader("📱 Connected Devices")
    devices = [
        ("📱 Samsung Galaxy S23", "Primary", "Delhi, India", "Active now"),
        ("⌚ Samsung Galaxy Watch", "Wearable", "Delhi, India", "Last seen 2h ago"),
    ]
    for device, dtype, location, last in devices:
        dc1, dc2, dc3, dc4 = st.columns([2, 1, 2, 1])
        with dc1: st.markdown(f"**{device}**")
        with dc2: st.caption(dtype)
        with dc3: st.caption(f"📍 {location} · {last}")
        with dc4: st.button("Remove", key=f"dev_{device}")
        st.markdown("---")

with tab4:
    st.subheader("ℹ️ About SafeHer AI")
    st.markdown(
        """
        **SafeHer AI** is an intelligent women's safety and emergency response system 
        that combines AI, GPS, voice recognition, and real-time communication to 
        provide proactive personal security.

        **Version:** 1.0.0  
        **Build:** June 2025  
        **Developer:** SafeHer AI Team  

        ---

        **🌐 SDG Alignment**
        - 🟣 **SDG 5** — Gender Equality
        - 🟢 **SDG 3** — Good Health and Well-being
        - 🔵 **SDG 11** — Sustainable Cities and Communities

        ---

        **🏗️ Tech Stack**
        - Frontend: Streamlit (Python)
        - AI/ML: TensorFlow Lite, NLP (spaCy, Transformers)
        - Maps: Folium + Google Maps API
        - Backend: Firebase (Auth, Firestore, Cloud Messaging)
        - Storage: Firebase Storage

        ---

        **📞 Support**
        - Email: support@safeherai.com
        - Website: www.safeherai.com
        - Emergency: Always call **100** (Police) or **181** (Women Helpline)
        """
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⭐ Rate This App", use_container_width=True):
            st.success("Thank you for your feedback!")
    with col2:
        if st.button("🐛 Report a Bug", use_container_width=True):
            st.info("Opening bug report form...")
