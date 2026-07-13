import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

# Try to load local .env if it exists (development fallback)
load_dotenv()

def get_gemini_api_key() -> str:
    """
    Retrieves the Gemini API Key using a fallback hierarchy:
    1. Streamlit Secrets (st.secrets)
    2. Environment Variable (os.getenv)
    """
    # 1. Check Streamlit secrets
    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
        
    # 2. Check environment variables (which might be populated by .env)
    return os.getenv("GEMINI_API_KEY", "")

@st.cache_resource
def _initialize_gemini(api_key: str):
    """
    Initializes the Gemini model. Cached to prevent multiple initializations.
    """
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-pro")

class AIService:
    """
    Dedicated AI Service for interacting with Google Gemini.
    Handles initialization, missing keys, and transient network failures.
    """
    
    def __init__(self):
        self.api_key = get_gemini_api_key()
        self.is_available = bool(self.api_key and self.api_key.strip())
        self.model = None
        
        if self.is_available:
            try:
                self.model = _initialize_gemini(self.api_key)
            except Exception as e:
                print(f"Failed to initialize Gemini: {e}")
                self.is_available = False

    def start_chat(self, history=None):
        """Starts a chat session if the model is available."""
        if not self.is_available or not self.model:
            return None
        return self.model.start_chat(history=history or [])

    # Retry transient failures (e.g., rate limits, network timeouts)
    @retry(
        wait=wait_exponential(multiplier=1, min=2, max=10),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(Exception), # Catch generic exceptions from the API
        reraise=True
    )
    def send_message(self, chat_session, prompt: str) -> str:
        """
        Sends a message to the chat session with exponential backoff for retries.
        """
        if not self.is_available or not chat_session:
            raise ValueError("AI Service is not available (Missing API Key or Initialization failed).")
            
        try:
            response = chat_session.send_message(prompt)
            return response.text
        except Exception as e:
            # We log the error securely in the terminal but do not leak to the user
            print(f"[AIService] Error calling Gemini: {e}")
            raise e
