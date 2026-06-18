# 🛡 SafeHer AI — Intelligent Women Safety & Emergency Response System

An AI-powered personal safety application built with Streamlit, providing real-time emergency response, live location tracking, voice-based risk detection, and family safety dashboards.

---

## 🚀 Live Demo

Deploy directly on [Streamlit Cloud](https://streamlit.io/cloud):

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/cloud)

---

## 📋 Features

| Module | Description |
|--------|-------------|
| 🏠 Dashboard | Safety overview, activity charts, quick SOS |
| 🚨 SOS Emergency | One-tap SOS with SMS + contact alert |
| 📍 Live Tracking | Real-time GPS map with route history |
| 🗺️ Safe Routes | AI-powered safest route recommendation |
| 🏥 Help Centers | Nearest police, hospitals, women helplines |
| 📞 Fake Call | Escape uncomfortable situations |
| 🤖 AI Risk Detection | NLP voice analysis + risk scoring |
| 📊 Emergency Dashboard | Family-facing safety monitor + evidence log |
| 👤 Profile | User settings, contacts, security |

---

## 🛠️ Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/SafeHerAI.git
cd SafeHerAI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Click **New App** → select your repository.
4. Set **Main file path** to `app.py`.
5. Click **Deploy**.

> No secrets or API keys required for the demo version.

---

## 📁 Project Structure

```
SafeHerAI/
├── app.py                          # Main dashboard
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                 # Streamlit theme & server config
├── pages/
│   ├── 1_🚨_SOS_Emergency.py
│   ├── 2_📍_Live_Tracking.py
│   ├── 3_🗺️_Safe_Routes.py
│   ├── 4_🏥_Help_Centers.py
│   ├── 5_📞_Fake_Call.py
│   ├── 6_🤖_AI_Risk_Detection.py
│   ├── 7_📊_Emergency_Dashboard.py
│   └── 8_👤_Profile.py
└── utils/
    └── helpers.py                  # Shared data helpers
```

---

## 🌐 SDG Alignment

- **SDG 5** — Gender Equality
- **SDG 3** — Good Health and Well-being
- **SDG 11** — Sustainable Cities and Communities

---

## 📄 License

MIT License — Free for educational and research use.
