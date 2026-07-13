import streamlit as st
from config.settings import THEME_COLOR_PRIMARY, THEME_COLOR_SECONDARY, THEME_BG_DARK, THEME_CARD_BG

def inject_custom_css():
    """Injects custom premium CSS for the SafeHer AI dashboard."""
    
    custom_css = f"""
    <style>
        /* Base Theme Overrides */
        .stApp {{
            background-color: {THEME_BG_DARK};
            color: #ffffff;
        }}
        
        /* Glassmorphism Cards */
        .glass-card {{
            background: rgba(26, 26, 46, 0.6);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }}
        .glass-card:hover {{
            transform: translateY(-5px);
            border: 1px solid rgba(233, 30, 140, 0.3);
        }}
        
        /* Metric Styling */
        [data-testid="stMetricValue"] {{
            font-size: 2rem !important;
            font-weight: 800 !important;
            color: {THEME_COLOR_PRIMARY} !important;
        }}
        
        /* Primary Buttons */
        .stButton > button[data-testid="baseButton-primary"] {{
            background: linear-gradient(90deg, {THEME_COLOR_PRIMARY} 0%, {THEME_COLOR_SECONDARY} 100%);
            border: none;
            border-radius: 12px;
            color: white;
            font-weight: bold;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }}
        
        .stButton > button[data-testid="baseButton-primary"]:hover {{
            opacity: 0.9;
            transform: scale(1.02);
            box-shadow: 0 0 15px rgba(233, 30, 140, 0.5);
        }}
        
        /* Secondary Buttons */
        .stButton > button[data-testid="baseButton-secondary"] {{
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            background: rgba(255, 255, 255, 0.05);
            transition: all 0.3s ease;
        }}
        
        .stButton > button[data-testid="baseButton-secondary"]:hover {{
            border: 1px solid {THEME_COLOR_PRIMARY};
            background: rgba(233, 30, 140, 0.1);
            color: {THEME_COLOR_PRIMARY};
        }}
        
        /* Text Inputs & Text Areas */
        .stTextInput > div > div > input, .stTextArea > div > div > textarea {{
            background-color: {THEME_CARD_BG};
            color: white;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {{
            border-color: {THEME_COLOR_PRIMARY};
            box-shadow: 0 0 0 1px {THEME_COLOR_PRIMARY};
        }}
        
        /* Selectbox */
        .stSelectbox > div > div > div {{
            background-color: {THEME_CARD_BG};
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {{
            background-color: {THEME_CARD_BG} !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }}
        
        /* Markdown / HTML specific classes */
        .gradient-text {{
            background: -webkit-linear-gradient(45deg, {THEME_COLOR_PRIMARY}, {THEME_COLOR_SECONDARY});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }}
        
        .pulse-animation {{
            animation: pulse 2s infinite;
        }}
        
        @keyframes pulse {{
            0% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(233, 30, 140, 0.7); }}
            70% {{ transform: scale(1.05); box-shadow: 0 0 0 10px rgba(233, 30, 140, 0); }}
            100% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(233, 30, 140, 0); }}
        }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
