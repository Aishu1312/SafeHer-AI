import streamlit as st
from deep_translator import GoogleTranslator

# Mapping of supported language names to Google Translate language codes.
# For regional languages not natively supported by Google Translate, we fallback to Hindi or nearest.
LANGUAGE_CODES = {
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
    # Graceful fallbacks for unsupported Google Translate dialects
    "Bodo": "hi",
    "Santali": "hi",
    "Tulu": "kn", # Closest regional script/context or just en/hi
    "Rajasthani": "hi",
    "Chhattisgarhi": "hi"
}

@st.cache_data(show_spinner=False)
def translate(text: str, target_lang_name: str) -> str:
    """
    Translates English text to the target language.
    Uses deep-translator with aggressive Streamlit caching.
    """
    if not text or not text.strip():
        return text
        
    if target_lang_name == "English" or target_lang_name == "English (International)":
        return text
        
    target_code = LANGUAGE_CODES.get(target_lang_name, "en")
    if target_code == "en":
        return text
        
    try:
        translator = GoogleTranslator(source='en', target=target_code)
        # Handle simple string translation
        translated = translator.translate(text)
        return translated if translated else text
    except Exception as e:
        print(f"Translation error for {text} to {target_lang_name}: {e}")
        return text

def _(text: str) -> str:
    """
    Helper function to translate text into the globally selected session language.
    If 'language' is not in session state, defaults to English.
    """
    target_lang = st.session_state.get('language', 'English')
    return translate(text, target_lang)
