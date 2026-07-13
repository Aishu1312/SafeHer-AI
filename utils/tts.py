import asyncio
import edge_tts
import base64
import os
import tempfile
import streamlit as st

# Voice mapping for neural voices based on language and caller type.
# Caller types: "Mother", "Father", "Sister", "Brother", "Friend", "Husband", "Wife", "Office", "Police", "Security"
# We define default genders for callers.
CALLER_GENDER = {
    "Mother": "Female",
    "Father": "Male",
    "Sister": "Female",
    "Brother": "Male",
    "Friend": "Female", # Defaulting to female friend
    "Husband": "Male",
    "Wife": "Female",
    "Office": "Female",
    "Police": "Male",
    "Security": "Male",
    "Custom": "Female"
}

# Supported Neural Voices in Edge TTS
VOICE_MAP = {
    "en": {"Female": "en-US-AriaNeural", "Male": "en-US-GuyNeural"},
    "hi": {"Female": "hi-IN-SwaraNeural", "Male": "hi-IN-MadhurNeural"},
    "mr": {"Female": "mr-IN-AarohiNeural", "Male": "mr-IN-ManoharNeural"},
    "gu": {"Female": "gu-IN-DhwaniNeural", "Male": "gu-IN-NiranjanNeural"},
    "ta": {"Female": "ta-IN-PallaviNeural", "Male": "ta-IN-ValluvarNeural"},
    "te": {"Female": "te-IN-ShrutiNeural", "Male": "te-IN-MohanNeural"},
    "kn": {"Female": "kn-IN-SapnaNeural", "Male": "kn-IN-GaganNeural"},
    "ml": {"Female": "ml-IN-SobhanaNeural", "Male": "ml-IN-MidhunNeural"},
    "bn": {"Female": "bn-IN-TanishaaNeural", "Male": "bn-IN-BashkarNeural"},
    "ur": {"Female": "ur-IN-GulNeural", "Male": "ur-IN-SalmanNeural"},
    # Fallback generic ones
    "default": {"Female": "en-US-AriaNeural", "Male": "en-US-GuyNeural"}
}

# We also map the language names to the short codes used in VOICE_MAP
LANG_TO_CODE = {
    "English": "en", "English (International)": "en",
    "Hindi": "hi", "Marathi": "mr", "Gujarati": "gu",
    "Tamil": "ta", "Telugu": "te", "Kannada": "kn",
    "Malayalam": "ml", "Bengali": "bn", "Urdu": "ur"
}

@st.cache_data(show_spinner=False)
def generate_tts_base64(text: str, caller_profile: str, language_name: str) -> str:
    """
    Generates realistic Neural TTS speech and returns it as a base64 encoded MP3 string.
    """
    if not text:
        return ""
        
    gender = CALLER_GENDER.get(caller_profile, "Female")
    lang_code = LANG_TO_CODE.get(language_name, "hi") # Default to Hindi if unsupported regional
    
    # Check if we have a neural voice for this language, else fallback to Hindi (most likely understood context in India) or English
    if lang_code not in VOICE_MAP:
        lang_code = "hi"
        
    voice = VOICE_MAP[lang_code][gender]
    
    # We use asyncio to run edge-tts which is asynchronous
    async def _generate():
        communicate = edge_tts.Communicate(text, voice)
        # Save to temp file
        fd, path = tempfile.mkstemp(suffix=".mp3")
        os.close(fd)
        await communicate.save(path)
        return path
        
    try:
        # Run the async function synchronously
        temp_path = asyncio.run(_generate())
        
        # Read the generated MP3
        with open(temp_path, "rb") as f:
            audio_bytes = f.read()
            
        # Clean up
        os.remove(temp_path)
        
        # Encode to base64
        return base64.b64encode(audio_bytes).decode()
    except Exception as e:
        print(f"TTS Generation Error: {e}")
        return ""
