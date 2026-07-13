import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

# Try to load local .env if it exists (development fallback)
load_dotenv()

def get_groq_api_key() -> str:
    """
    Retrieves the Groq API Key using a fallback hierarchy:
    1. Streamlit Secrets (st.secrets)
    2. Environment Variable (os.getenv)
    """
    # 1. Check Streamlit secrets
    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass
        
    # 2. Check environment variables (which might be populated by .env)
    return os.getenv("GROQ_API_KEY", "")

@st.cache_resource
def _initialize_groq(api_key: str):
    """
    Initializes the Groq client. Cached to prevent multiple initializations.
    """
    return Groq(api_key=api_key)

class AIService:
    """
    Dedicated AI Service for interacting with Groq.
    Handles initialization, missing keys, and transient network failures.
    """
    
    def __init__(self):
        self.api_key = get_groq_api_key()
        self.is_available = bool(self.api_key and self.api_key.strip())
        self.client = None
        self.model = "llama3-70b-8192" # Fast and high capability
        
        if self.is_available:
            try:
                self.client = _initialize_groq(self.api_key)
            except Exception as e:
                print(f"Failed to initialize Groq: {e}")
                self.is_available = False

    def start_chat(self, history=None):
        """Returns a dummy chat session object for UI compatibility."""
        return "groq_chat_session"

    # Retry transient failures (e.g., rate limits, network timeouts)
    @retry(
        wait=wait_exponential(multiplier=1, min=2, max=10),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(Exception),
        reraise=True
    )
    def send_message(self, message_history: list) -> str:
        """
        Sends the entire message history to Groq and returns the response.
        message_history should be a list of {"role": ..., "content": ...}
        """
        if not self.is_available or not self.client:
            raise ValueError("AI Service is not available (Missing API Key or Initialization failed).")
            
        try:
            # We filter out system instructions if any, or just pass them as standard messages
            response = self.client.chat.completions.create(
                messages=message_history,
                model=self.model,
                temperature=0.7,
                max_tokens=1024
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"[AIService] Error calling Groq: {e}")
            raise e
