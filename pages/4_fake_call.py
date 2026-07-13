import streamlit as st
import time
import base64
from styles.css import inject_custom_css
from components.fake_call_ui import render_fake_call

st.set_page_config(page_title="Fake Call - SafeHer AI", page_icon="📞", layout="wide")
inject_custom_css()

st.title("📞 Fake Call Generator")
st.caption("Escape uncomfortable situations with a simulated incoming call")
st.markdown("---")

col1, col2 = st.columns([1, 1])

# Initialize session state for fake call
if 'fc_triggered' not in st.session_state:
    st.session_state.fc_triggered = False
if 'fc_time' not in st.session_state:
    st.session_state.fc_time = 0
if 'fc_caller' not in st.session_state:
    st.session_state.fc_caller = "Mom"
if 'fc_voice_base64' not in st.session_state:
    st.session_state.fc_voice_base64 = ""
if 'fc_ringtone' not in st.session_state:
    st.session_state.fc_ringtone = "https://actions.google.com/sounds/v1/alarms/phone_ringing.ogg"

with col1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("⚙️ Call Settings")
    
    # 1. Caller Profile
    caller_profile = st.selectbox("Caller Profile", ["Mom", "Dad", "Sister", "Brother", "Friend", "Husband", "Wife", "Office", "Police", "Security", "Custom"])
    if caller_profile == "Custom":
        caller_name = st.text_input("Custom Caller Name", value="Unknown")
    else:
        caller_name = caller_profile
        
    # 2. Schedule Delay
    delay = st.selectbox("Trigger Delay", ["Immediately", "10 seconds", "15 seconds", "30 seconds", "1 minute", "2 minutes", "5 minutes", "Custom"])
    if delay == "Custom":
        custom_delay = st.number_input("Custom Delay (seconds)", min_value=0, max_value=3600, value=60)
        delay_seconds = custom_delay
    else:
        delay_map = {
            "Immediately": 0,
            "10 seconds": 10,
            "15 seconds": 15,
            "30 seconds": 30,
            "1 minute": 60,
            "2 minutes": 120,
            "5 minutes": 300
        }
        delay_seconds = delay_map[delay]
        
    # 3. Custom Voice Message
    st.markdown("---")
    st.subheader("🎙️ Voice Message on Answer")
    voice_type = st.radio("Select Audio Source", ["Preset Message", "Upload Custom Audio"])
    voice_b64 = ""
    
    if voice_type == "Preset Message":
        preset = st.selectbox("Preset Message", [
            "Hi, where are you? I'm outside waiting.",
            "I'm almost there. Can you come out?",
            "I've reached your location."
        ])
        # Since we don't have these files locally, we will just use a generic beep or empty 
        # unless user uploads. For now, leave empty base64 to fallback to silence or generic.
        # In a real app we would load a local preset MP3 file.
    else:
        uploaded_file = st.file_uploader("Upload MP3/WAV", type=["mp3", "wav", "ogg"])
        if uploaded_file is not None:
            audio_bytes = uploaded_file.read()
            voice_b64 = base64.b64encode(audio_bytes).decode()
            st.audio(audio_bytes, format='audio/mp3')

    st.markdown("---")
    
    if st.button("🚨 Start Fake Call", type="primary", use_container_width=True):
        st.session_state.fc_triggered = True
        st.session_state.fc_time = time.time() + delay_seconds
        st.session_state.fc_caller = caller_name
        st.session_state.fc_voice_base64 = voice_b64
        st.success(f"Fake call from {caller_name} scheduled!")
        
    if st.session_state.fc_triggered:
        if st.button("⏹️ Cancel Schedule", use_container_width=True):
            st.session_state.fc_triggered = False
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if st.session_state.fc_triggered:
        time_left = st.session_state.fc_time - time.time()
        
        if time_left > 0:
            st.markdown("<div class='glass-card' style='text-align:center;'>", unsafe_allow_html=True)
            st.info(f"### ⏳ Call scheduled")
            
            # Create an empty placeholder for the countdown
            countdown_placeholder = st.empty()
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Simple Streamlit countdown loop
            while time_left > 0:
                mins, secs = divmod(int(time_left), 60)
                countdown_placeholder.markdown(f"**Incoming call in:** `{mins:02d}:{secs:02d}`")
                time.sleep(1)
                time_left = st.session_state.fc_time - time.time()
                
            st.rerun()
        else:
            # Render the UI component
            render_fake_call(
                caller_name=st.session_state.fc_caller,
                voice_base64=st.session_state.fc_voice_base64,
                ringtone_url=st.session_state.fc_ringtone
            )
            
            if st.button("Reset Fake Call"):
                st.session_state.fc_triggered = False
                st.rerun()
    else:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center; padding: 40px 0; color: #aaa;">
            <p style="font-size: 80px; margin: 0; opacity: 0.5;">📱</p>
            <h3>Ready</h3>
            <p>Configure your fake call settings and press Start.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
