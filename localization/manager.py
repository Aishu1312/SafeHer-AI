import os
import json
import streamlit as st

# Language codes matching the JSON files
LANG_CODES = {
    "English": "en",
    "English (International)": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Assamese": "as",
    "Odia": "or",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Urdu": "ur",
    "Sanskrit": "sa",
    "Konkani": "gom",
    "Nepali": "ne",
    "Manipuri": "mni-Mtei",
    "Dogri": "doi",
    "Kashmiri": "ks",
    "Sindhi": "sd",
    "Maithili": "mai",
    "Bhojpuri": "bho",
    # Regional fallbacks
    "Bodo": "hi",
    "Santali": "hi",
    "Tulu": "kn",
    "Rajasthani": "hi",
    "Chhattisgarhi": "hi"
}

@st.cache_data
def _load_translations(lang_code: str) -> dict:
    """Loads a specific JSON language file and caches it into memory."""
    if not lang_code:
        lang_code = "en"
        
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "translations", f"{lang_code}.json")
    
    if not os.path.exists(file_path):
        # Fallback to English if file doesn't exist
        file_path = os.path.join(base_dir, "translations", "en.json")
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading translation file {file_path}: {e}")
        return {}

def _(text: str) -> str:
    """
    Translates a given English string into the globally selected language.
    Reads from the cached JSON dictionary for instantaneous lookup.
    """
    if not text or not text.strip():
        return text
        
    lang_name = st.session_state.get('language', 'English')
    lang_code = LANG_CODES.get(lang_name, "en")
    
    # Fast path for English
    if lang_code == "en":
        return text
        
    # Load dictionary for the target language
    translations = _load_translations(lang_code)
    
    # Return translated string, fallback to English original if missing
    return translations.get(text, text)
