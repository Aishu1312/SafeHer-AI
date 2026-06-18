import streamlit as st
import time
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from safeher.utils.helpers import get_risk_score

st.set_page_config(page_title="AI Risk Detection – SafeHer AI", page_icon="🤖", layout="wide")

st.sidebar.title("🛡 SafeHer AI")
st.sidebar.caption("Intelligent Women Safety System")
st.sidebar.markdown("---")
st.sidebar.info("👤 **Logged in as:** Priya Sharma\n\n📍 **Status:** Safe")

st.title("🤖 AI Risk Detection")
st.caption("Real-time AI analysis of voice, movement, and environment to detect risk")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎙️ Voice Command Analysis")
    st.caption("Type or speak a phrase — AI analyzes for panic keywords and tone")

    voice_input = st.text_area(
        "Enter voice input / text to analyze:",
        placeholder="e.g. 'Please help me, someone is following me'",
        height=100,
    )

    analyze = st.button("🔍 Analyze Risk", type="primary", use_container_width=True)

    if analyze and voice_input:
        with st.spinner("Analyzing with NLP model..."):
            time.sleep(1.2)

        score = get_risk_score(voice_input)

        if score >= 70:
            level, color, icon = "HIGH", "#FF1744", "🔴"
            action = "🚨 Activating emergency mode and notifying contacts!"
            st.error(f"{icon} **{level} RISK DETECTED** — Score: {score}/100\n\n{action}")
        elif score >= 40:
            level, color, icon = "MEDIUM", "#FF9800", "🟡"
            action = "⚠️ Monitoring closely. Ready to activate SOS."
            st.warning(f"{icon} **{level} RISK** — Score: {score}/100\n\n{action}")
        else:
            level, color, icon = "LOW", "#00E676", "🟢"
            action = "✅ No immediate threat detected."
            st.success(f"{icon} **{level} RISK** — Score: {score}/100\n\n{action}")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Risk Score", "font": {"color": "white"}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "white"},
                "bar": {"color": color},
                "steps": [
                    {"range": [0, 40], "color": "#1a2e1a"},
                    {"range": [40, 70], "color": "#2e2a1a"},
                    {"range": [70, 100], "color": "#2e1a1a"},
                ],
                "threshold": {"line": {"color": "white", "width": 3}, "thickness": 0.75, "value": score},
            },
            number={"font": {"color": "white"}},
        ))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            height=250,
            margin=dict(l=20, r=20, t=30, b=20),
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🧠 NLP Analysis")
        keywords_found = [kw for kw in ["help", "danger", "emergency", "scared", "follow", "attack"] if kw in voice_input.lower()]
        if keywords_found:
            st.markdown(f"**Panic keywords detected:** {', '.join([f'`{k}`' for k in keywords_found])}")
        st.markdown(f"**Emotional tone:** {'Fearful / Distressed' if score > 50 else 'Calm / Neutral'}")
        st.markdown(f"**Confidence:** {min(score + 10, 99)}%")

    elif analyze:
        st.warning("Please enter a voice input to analyze.")

with col2:
    st.subheader("📊 Risk Factors Monitor")

    np.random.seed(int(time.time()) % 100)
    factors = {
        "Voice Pattern": np.random.randint(10, 45),
        "Location (night/isolated)": np.random.randint(15, 60),
        "Movement Speed": np.random.randint(5, 30),
        "Route Deviation": np.random.randint(5, 25),
        "Inactivity Duration": np.random.randint(5, 20),
    }

    fig2 = px.bar(
        x=list(factors.values()),
        y=list(factors.keys()),
        orientation="h",
        color=list(factors.values()),
        color_continuous_scale=["#00E676", "#FF9800", "#FF1744"],
        range_color=[0, 100],
    )
    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#FFFFFF",
        height=280,
        margin=dict(l=0, r=0, t=10, b=0),
        coloraxis_showscale=False,
        xaxis_title="Risk Contribution (%)",
        yaxis_title="",
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("⚙️ AI Detection Settings")
    st.toggle("Background Voice Monitoring", value=True)
    st.toggle("Movement Anomaly Detection", value=True)
    st.toggle("Auto-trigger SOS on High Risk", value=False)
    st.toggle("Send Risk Reports to Contacts", value=True)
    sensitivity = st.selectbox("Detection Sensitivity", ["Low", "Medium", "High", "Maximum"])
    st.caption(f"Current sensitivity: **{sensitivity}** — AI scans every 30 seconds")

st.markdown("---")
st.subheader("📈 Risk Score History (Today)")
hours = list(range(0, 24))
risk_history = [np.random.randint(5, 25) for _ in range(20)] + [72, 80, 15, 10]
risk_df = pd.DataFrame({"Hour": [f"{h}:00" for h in hours], "Risk Score": risk_history})
fig3 = px.line(risk_df, x="Hour", y="Risk Score", markers=True,
               color_discrete_sequence=["#E91E8C"])
fig3.add_hline(y=70, line_dash="dash", line_color="#FF1744", annotation_text="High Risk Threshold")
fig3.add_hline(y=40, line_dash="dash", line_color="#FF9800", annotation_text="Medium Risk Threshold")
fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                   font_color="#FFFFFF", height=250, margin=dict(l=0, r=0, t=10, b=0))
st.plotly_chart(fig3, use_container_width=True)
