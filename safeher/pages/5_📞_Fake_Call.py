import streamlit as st
import time
import random

st.set_page_config(page_title="Fake Call – SafeHer AI", page_icon="📞", layout="wide")

st.sidebar.title("🛡 SafeHer AI")
st.sidebar.caption("Intelligent Women Safety System")
st.sidebar.markdown("---")
st.sidebar.info("👤 **Logged in as:** Priya Sharma\n\n📍 **Status:** Safe")

st.title("📞 Fake Call Generator")
st.caption("Escape uncomfortable situations with a simulated incoming call")

st.markdown("---")
st.info(
    "💡 **How it works:** Press 'Trigger Fake Call' below. "
    "It will simulate an incoming call — use it to safely excuse yourself from any uncomfortable situation."
)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("⚙️ Call Settings")

    caller_name = st.text_input("Caller Name", value="Mom")
    delay = st.slider("Call Delay (seconds)", 0, 30, 5, 1)
    duration = st.slider("Call Duration (seconds)", 10, 120, 30, 5)
    ringtone = st.selectbox("Ringtone Style", ["Default Ring", "Vibrate Only", "Custom Tone 1", "Custom Tone 2"])
    voice_msg = st.selectbox(
        "Pre-recorded Voice Message",
        [
            "Hey, are you okay? Where are you?",
            "Come home right now, it's urgent!",
            "I'm waiting outside, come quickly.",
            "The meeting got cancelled, come back.",
        ]
    )

    trigger = st.button("📞 Trigger Fake Call", type="primary", use_container_width=True)

    if trigger:
        if delay > 0:
            with st.spinner(f"Fake call incoming in {delay} seconds..."):
                time.sleep(min(delay, 3))
        st.markdown(
            f"""
            <div style='
                background: linear-gradient(135deg, #1a1a2e, #0f0f1a);
                border: 2px solid #E91E8C;
                border-radius: 20px;
                padding: 30px;
                text-align: center;
                margin: 10px 0;
            '>
                <p style='font-size: 14px; color: #aaa; margin: 0;'>Incoming Call</p>
                <p style='font-size: 32px; font-weight: bold; color: #fff; margin: 8px 0;'>📱 {caller_name}</p>
                <p style='font-size: 14px; color: #E91E8C; margin: 0;'>Mobile · {ringtone}</p>
                <br/>
                <p style='font-size: 28px; margin: 0;'>🟢 &nbsp;&nbsp;&nbsp; 🔴</p>
                <p style='font-size: 12px; color: #888; margin: 4px 0;'>Accept &nbsp;&nbsp;&nbsp;&nbsp; Decline</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.success(f"📞 Incoming call from **{caller_name}** — Duration: {duration}s")

with col2:
    st.subheader("📋 Quick Contacts for Fake Calls")
    quick_contacts = [
        ("Mom", "Family", "🟢"),
        ("Dad", "Family", "🟢"),
        ("Sister", "Family", "🟡"),
        ("Best Friend", "Friend", "🟢"),
        ("Boss", "Work", "🟢"),
        ("Doctor", "Professional", "🟡"),
    ]

    for name, category, status in quick_contacts:
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1:
            st.markdown(f"{status} **{name}** · *{category}*")
        with c2:
            if st.button("⚡ Quick", key=f"quick_{name}"):
                st.success(f"📞 Fake call from {name} in 3s!")
        st.markdown("---")

    st.subheader("➕ Add Custom Caller")
    with st.form("custom_caller"):
        new_caller = st.text_input("Name")
        new_number = st.text_input("Display Number (optional)")
        if st.form_submit_button("Add Caller"):
            if new_caller:
                st.success(f"✅ '{new_caller}' added to fake callers list!")

st.markdown("---")
st.subheader("💡 Safety Tips")
tips = [
    "🟢 Use the fake call feature if someone is following you in public.",
    "🟡 Set the delay to 0 for an immediate call when you feel unsafe.",
    "🔵 Use 'Boss' or 'Doctor' as callers for workplace uncomfortable situations.",
    "🟣 Combine with the SOS feature for maximum safety.",
]
for tip in tips:
    st.markdown(tip)
