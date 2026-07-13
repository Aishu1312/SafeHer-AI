import streamlit as st
import time
import base64
import random
from styles.css import inject_custom_css
from components.fake_call_ui import render_fake_call
from localization.manager import _
from utils.tts import generate_tts_base64

st.set_page_config(page_title=_("Fake Call") + " - SafeHer AI", page_icon="📞", layout="wide")
inject_custom_css()

st.title(f"📞 {_('Fake Call Generator')}")
st.caption(_("Escape uncomfortable situations with a simulated incoming call"))
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

# Context-aware scripts for realistic conversation
CALLER_SCRIPTS = {
    "Mom": [
        "Hello dear, where are you? I've been waiting for you.",
        "I'm outside. Can you come quickly?",
        "Your father and I are here. Please answer.",
        "Call me back if you can't talk."
    ],
    "Dad": [
        "Hey, are you okay? I'm coming to pick you up.",
        "Where are you? Send me your location now.",
        "I'm outside waiting in the car."
    ],
    "Friend": [
        "Hey! I'm waiting outside.",
        "Where are you? We're getting late.",
        "Hey, I booked the cab. Are you coming?"
    ],
    "Office": [
        "Hello, this is the office. We need you to join the emergency meeting.",
        "Hi, your manager is asking for you.",
    ],
    "Police": [
        "Hello, this is the local police station. We received an alert.",
        "Is everything okay? We are tracking your location."
    ],
    "Security": [
        "Hello ma'am, your cab is waiting downstairs.",
        "Security here. Please confirm your entry."
    ],
    "Default": [
        "Hello, can you hear me? Where are you?",
        "I've been trying to reach you. Please call me back."
    ]
}

with col1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader(f"⚙️ {_('Call Settings')}")
    
    # 1. Caller Profile
    caller_options = [_("Mom"), _("Dad"), _("Sister"), _("Brother"), _("Friend"), _("Husband"), _("Wife"), _("Office"), _("Police"), _("Security"), _("Custom")]
    caller_profile_display = st.selectbox(_("Caller Profile"), caller_options)
    
    # Map back to English keys for our logic
    english_keys = ["Mom", "Dad", "Sister", "Brother", "Friend", "Husband", "Wife", "Office", "Police", "Security", "Custom"]
    caller_profile = english_keys[caller_options.index(caller_profile_display)]
    
    if caller_profile == "Custom":
        caller_name = st.text_input(_("Custom Caller Name"), value=_("Unknown"))
    else:
        caller_name = caller_profile_display
        
    # 2. Schedule Delay
    delay_opts = [_("Immediately"), _("10 seconds"), _("15 seconds"), _("30 seconds"), _("1 minute"), _("2 minutes"), _("5 minutes"), _("Custom")]
    delay = st.selectbox(_("Trigger Delay"), delay_opts)
    
    if delay == _("Custom"):
        custom_delay = st.number_input(_("Custom Delay (seconds)"), min_value=0, max_value=3600, value=60)
        delay_seconds = custom_delay
    else:
        delay_map = {
            _("Immediately"): 0, _("10 seconds"): 10, _("15 seconds"): 15,
            _("30 seconds"): 30, _("1 minute"): 60, _("2 minutes"): 120, _("5 minutes"): 300
        }
        delay_seconds = delay_map[delay]
        
    # 3. Custom Voice Message
    st.markdown("---")
    st.subheader(f"🎙️ {_('Voice Message on Answer')}")
    voice_type = st.radio(_("Select Audio Source"), [_("Neural AI Voice (Realistic)"), _("Upload Custom Audio")])
    
    uploaded_audio_b64 = ""
    if voice_type == _("Upload Custom Audio"):
        uploaded_file = st.file_uploader(_("Upload MP3/WAV"), type=["mp3", "wav", "ogg"])
        if uploaded_file is not None:
            audio_bytes = uploaded_file.read()
            uploaded_audio_b64 = base64.b64encode(audio_bytes).decode()
            st.audio(audio_bytes, format='audio/mp3')

    st.markdown("---")
    
    if st.button(f"🚨 {_('Start Fake Call')}", type="primary", use_container_width=True):
        st.session_state.fc_triggered = True
        st.session_state.fc_time = time.time() + delay_seconds
        st.session_state.fc_caller = caller_name
        
        if voice_type == _("Upload Custom Audio") and uploaded_audio_b64:
            st.session_state.fc_voice_base64 = uploaded_audio_b64
        else:
            # Generate Neural AI Voice dynamically
            scripts = CALLER_SCRIPTS.get(caller_profile, CALLER_SCRIPTS["Default"])
            script = random.choice(scripts)
            
            # Translate the script into the selected language
            translated_script = _(script)
            
            # Generate TTS in the selected language
            with st.spinner(_("Generating realistic voice...")):
                b64_audio = generate_tts_base64(translated_script, caller_profile, st.session_state.language)
                st.session_state.fc_voice_base64 = b64_audio
                
        st.success(_("Fake call scheduled!"))
        
    if st.session_state.fc_triggered:
        if st.button(f"⏹️ {_('Cancel Schedule')}", use_container_width=True):
            st.session_state.fc_triggered = False
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if st.session_state.fc_triggered:
        time_left = st.session_state.fc_time - time.time()
        
        if time_left > 0:
            st.markdown("<div class='glass-card' style='text-align:center;'>", unsafe_allow_html=True)
            st.info(f"### ⏳ {_('Call scheduled')}")
            
            countdown_placeholder = st.empty()
            st.markdown("</div>", unsafe_allow_html=True)
            
            while time_left > 0:
                mins, secs = divmod(int(time_left), 60)
                countdown_placeholder.markdown(f"**{_('Incoming call in')}:** `{mins:02d}:{secs:02d}`")
                time.sleep(1)
                time_left = st.session_state.fc_time - time.time()
                
            st.rerun()
        else:
            render_fake_call(
                caller_name=st.session_state.fc_caller,
                voice_base64=st.session_state.fc_voice_base64,
                ringtone_url=st.session_state.fc_ringtone,
                lang_data={
                    "incoming": _("Incoming Call"),
                    "mobile": _("Mobile"),
                    "accept": _("Accept"),
                    "decline": _("Decline"),
                    "ended": _("Call Ended"),
                    "declined": _("Call Declined")
                }
            )
            
            if st.button(_("Reset Fake Call")):
                st.session_state.fc_triggered = False
                st.rerun()
    else:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="text-align: center; padding: 40px 0; color: #aaa;">
            <p style="font-size: 80px; margin: 0; opacity: 0.5;">📱</p>
            <h3>{_('Ready')}</h3>
            <p>{_('Configure your fake call settings and press Start.')}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
