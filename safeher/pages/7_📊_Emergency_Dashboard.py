import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime
import numpy as np

st.set_page_config(page_title="Emergency Dashboard – SafeHer AI", page_icon="📊", layout="wide")

st.sidebar.title("🛡 SafeHer AI")
st.sidebar.caption("Intelligent Women Safety System")
st.sidebar.markdown("---")
st.sidebar.info("👤 **Family Dashboard:** Sharma Family\n\n📍 **Watching:** Priya")

st.title("📊 Emergency Dashboard")
st.caption("Real-time safety status for family members and trusted contacts")

st.markdown("---")

st.subheader("👨‍👩‍👧 Members Being Tracked")
member_cols = st.columns(3)
members = [
    ("Priya Sharma", "🟢 Safe", "Connaught Place, Delhi", "10:34 AM", "Low (18%)"),
    ("Anjali Verma", "🟢 Safe", "Lajpat Nagar, Delhi", "10:28 AM", "Low (12%)"),
    ("Meera Kapoor", "🟡 Caution", "Isolated road, Gurgaon", "10:31 AM", "Medium (54%)"),
]

for i, (name, status, location, time_val, risk) in enumerate(members):
    with member_cols[i]:
        color = "#00E676" if "Safe" in status else "#FF9800"
        st.markdown(
            f"""
            <div style='border:1px solid {color}; border-radius:10px; padding:15px; text-align:center;'>
                <p style='font-size:28px; margin:0;'>👩</p>
                <p style='font-weight:bold; margin:4px 0;'>{name}</p>
                <p style='color:{color}; margin:4px 0;'>{status}</p>
                <p style='font-size:12px; color:#aaa; margin:2px 0;'>📍 {location}</p>
                <p style='font-size:12px; color:#aaa; margin:2px 0;'>⏱ Updated {time_val}</p>
                <p style='font-size:12px; margin:2px 0;'>⚠️ Risk: {risk}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🚨 Live Alert Feed")
    alerts = [
        ("10:31 AM", "🟡 CAUTION", "Meera", "Route deviation detected — 2.3km off planned path"),
        ("10:15 AM", "🟢 INFO", "Priya", "Journey started from Rajouri Garden"),
        ("09:45 AM", "🟢 INFO", "Anjali", "Reached destination safely"),
        ("Yesterday 11:30 PM", "🔴 SOS", "Priya", "SOS triggered — resolved by user in 2 min"),
        ("Yesterday 8:15 PM", "🟡 CAUTION", "Meera", "Inactivity detected for 15 min — auto-checked"),
    ]

    for time_val, level, member, event in alerts:
        color = "#FF1744" if "SOS" in level else ("#FF9800" if "CAUTION" in level else "#00E676")
        st.markdown(
            f"<div style='border-left:3px solid {color}; padding:8px 12px; margin:6px 0; background:rgba(255,255,255,0.03); border-radius:0 8px 8px 0;'>"
            f"<span style='color:{color}; font-weight:bold;'>{level}</span> &nbsp; "
            f"<span style='color:#aaa; font-size:12px;'>{time_val}</span><br/>"
            f"<strong>{member}</strong> — {event}"
            f"</div>",
            unsafe_allow_html=True,
        )

with col2:
    st.subheader("📋 Evidence Log")
    evidence = pd.DataFrame({
        "Time": ["10:31 AM", "Yesterday 11:30 PM", "2 days ago 9 PM"],
        "Type": ["📍 Location", "🎙 Audio", "📸 Photo"],
        "Event": ["Route deviation", "SOS activated", "Manual capture"],
        "Status": ["Saved", "Saved", "Saved"],
    })
    st.dataframe(evidence, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.subheader("📥 Export Report")
    report_type = st.selectbox("Report Type", ["Daily Summary", "Weekly Report", "Incident Report", "Full History"])
    if st.button("📥 Generate & Download", use_container_width=True):
        sample_csv = pd.DataFrame({
            "Date": pd.date_range(end=datetime.date.today(), periods=5),
            "Member": ["Priya", "Meera", "Anjali", "Priya", "Meera"],
            "Event": ["SOS", "Route Deviation", "Safe Arrival", "Journey Start", "Check-In"],
            "Location": ["Delhi", "Gurgaon", "Delhi", "Delhi", "Gurgaon"],
            "Risk": ["High", "Medium", "Low", "Low", "Low"],
        })
        csv_data = sample_csv.to_csv(index=False)
        st.download_button(
            "⬇️ Download CSV",
            data=csv_data,
            file_name=f"safeher_report_{datetime.date.today()}.csv",
            mime="text/csv",
            use_container_width=True,
        )

st.markdown("---")
st.subheader("📅 Weekly Safety Overview")
dates = pd.date_range(end=datetime.date.today(), periods=7)
weekly = pd.DataFrame({
    "Date": dates,
    "Priya Risk Score": np.random.randint(10, 40, 7),
    "Meera Risk Score": np.random.randint(20, 70, 7),
    "Anjali Risk Score": np.random.randint(5, 30, 7),
})
fig = px.line(
    weekly, x="Date",
    y=["Priya Risk Score", "Meera Risk Score", "Anjali Risk Score"],
    markers=True,
    color_discrete_map={
        "Priya Risk Score": "#E91E8C",
        "Meera Risk Score": "#FF9800",
        "Anjali Risk Score": "#00BCD4",
    },
)
fig.add_hline(y=70, line_dash="dash", line_color="#FF1744", annotation_text="High Risk")
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font_color="#FFFFFF", height=280, margin=dict(l=0, r=0, t=10, b=0),
)
st.plotly_chart(fig, use_container_width=True)
