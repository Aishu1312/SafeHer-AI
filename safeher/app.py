import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime
import random
from safeher.utils.helpers import get_mock_alerts, get_activity_data

st.set_page_config(
    page_title="SafeHer AI",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("🛡 SafeHer AI")
st.sidebar.caption("Intelligent Women Safety System")
st.sidebar.markdown("---")
st.sidebar.info("👤 **Logged in as:** Priya Sharma\n\n📍 **Status:** Safe")
st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Emergency Numbers**\n"
    "- 🚔 Police: **100**\n"
    "- 🏥 Ambulance: **102**\n"
    "- 🆘 Women Helpline: **181**\n"
    "- 🔥 Fire: **101**"
)

st.title("🛡 SafeHer AI — Dashboard")
st.caption("Your intelligent personal safety companion")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Safety Status", "✅ Safe", delta="All Clear")
with col2:
    st.metric("Trusted Contacts", "3", delta="Active")
with col3:
    st.metric("Alerts This Week", "2", delta="-1 vs last week")
with col4:
    st.metric("Risk Score", "Low (18%)", delta="-5%")

st.markdown("---")

col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📊 30-Day Activity Overview")
    activity = get_activity_data()
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=activity["Date"], y=activity["Trips"],
        name="Daily Trips", marker_color="#E91E8C", opacity=0.8
    ))
    fig.add_trace(go.Scatter(
        x=activity["Date"], y=activity["Risk Score"],
        name="Risk Score", mode="lines+markers",
        line=dict(color="#FF6B35", width=2),
        yaxis="y2"
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#FFFFFF",
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        yaxis2=dict(overlaying="y", side="right", title="Risk Score"),
        height=300,
        margin=dict(l=0, r=0, t=10, b=0),
    )
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🔔 Alert Distribution")
    labels = ["SOS Triggered", "Voice Command", "Manual Alert", "Route Deviation"]
    values = [3, 5, 2, 1]
    fig2 = go.Figure(data=[go.Pie(
        labels=labels, values=values,
        hole=0.45,
        marker_colors=["#E91E8C", "#FF6B35", "#7B2FBE", "#00BCD4"]
    )])
    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#FFFFFF",
        showlegend=True,
        height=300,
        margin=dict(l=0, r=0, t=10, b=0),
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.subheader("🕒 Recent Alerts")
alerts_df = get_mock_alerts()
st.dataframe(alerts_df, use_container_width=True, hide_index=True)

st.markdown("---")
st.subheader("🚀 Quick Actions")
qc1, qc2, qc3, qc4 = st.columns(4)
with qc1:
    if st.button("🚨 Trigger SOS", use_container_width=True, type="primary"):
        st.error("🚨 SOS Activated! Notifying your trusted contacts and emergency services...")
with qc2:
    if st.button("📍 Share Location", use_container_width=True):
        st.success("✅ Live location shared with 3 trusted contacts!")
with qc3:
    if st.button("🏥 Find Help Centers", use_container_width=True):
        st.info("📍 Opening nearby help centers map...")
with qc4:
    if st.button("📞 Fake Call", use_container_width=True):
        st.info("📞 Initiating fake call from 'Mom'...")

st.markdown("---")
st.caption("SafeHer AI v1.0 · Built for Women's Safety · SDG 5 · SDG 3 · SDG 11")
