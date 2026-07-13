# 🛡️ SafeHer AI – Intelligent Women Safety Platform

SafeHer AI is a production-ready, highly polished Streamlit application designed to provide proactive personal security for women. It combines real-time GPS tracking, AI-powered conversational assistance, and one-tap emergency response to create a comprehensive safety ecosystem.

## ✨ Features

- **🔐 Secure User Profiles**: Personalized dashboard with dynamic emergency contacts and medical information.
- **📍 Live Location Sharing**: Automatically fetches browser GPS coordinates and generates instant sharing links for WhatsApp, SMS, and Maps.
- **🚨 1-Tap SOS Emergency**: Triggers immediate alerts containing live location, time, and distress messages to all trusted contacts.
- **📞 Fake Call Generator**: Escapes uncomfortable situations by simulating an incoming call with a realistic UI, countdown timer, and mock audio.
- **🏥 Nearby Help Centers**: Dynamically locates the nearest police stations, hospitals, and NGOs with 1-click navigation and dialing.
- **🤖 Multilingual AI Safety Assistant**: Integrated with Gemini 1.5 Pro to provide safety advice, legal rights, and mental support in 10+ Indian languages.
- **💎 Premium UI/UX**: Features a Glassmorphism design, dark mode aesthetics, smooth animations, and a fully responsive layout optimized for mobile and desktop.

## 🏗️ Architecture & Folder Structure

The application follows a clean, modular architecture:

```text
SafeHer-AI/
├── .streamlit/
│   └── config.toml          # Streamlit theme and settings
├── components/              # Reusable Streamlit UI components
├── config/                  # Configuration, constants, and settings
├── pages/                   # Streamlit multipage files (only visible post-login)
├── styles/                  # Custom CSS (glassmorphism, animations)
├── utils/                   # Helper functions (session management)
├── app.py                   # Main entry point (Authentication & Routing)
└── requirements.txt         # Optimized dependencies
```

## 🛠️ Tech Stack

- **Frontend**: Streamlit, HTML5, CSS3
- **Mapping**: Folium, Streamlit-Folium
- **Geolocation**: Streamlit-Geolocation, Geopy
- **AI Integration**: Google Generative AI (Gemini 1.5 Pro)
- **Data & APIs**: Google Maps Search URLs, WhatsApp API

## 🚀 Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aishu1312/SafeHer-AI.git
   cd SafeHer-AI
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure Secrets:**
   Create a `.streamlit/secrets.toml` file in the root directory and add your Gemini API Key:
   ```toml
   GEMINI_API_KEY = "your_google_gemini_api_key_here"
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## ☁️ Deployment

SafeHer AI is optimized for **Streamlit Community Cloud**. 

1. Push your code to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and link your repository.
3. In the advanced settings of your Streamlit deployment, add the `GEMINI_API_KEY` under the "Secrets" section.
4. Deploy! The app will install everything from `requirements.txt` and launch successfully.

## 🚀 Future Scope

- **Voice SOS Activation**: Hands-free emergency trigger using keyword recognition.
- **Safe Route Suggestions**: AI-powered navigation avoiding high-risk or poorly lit areas.
- **Offline Mode**: SMS-based fallback when the internet is unavailable.
- **Hardware Integration**: Smartwatch and panic button IoT integration.

## 📄 License

This project is open-source and available under the MIT License.

## 🤝 Contributors

Built with ❤️ for women's safety.
