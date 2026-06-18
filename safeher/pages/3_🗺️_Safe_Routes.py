import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(page_title="Safe Routes – SafeHer AI", page_icon="🗺️", layout="wide")

st.sidebar.title("🛡 SafeHer AI")
st.sidebar.caption("Intelligent Women Safety System")
st.sidebar.markdown("---")
st.sidebar.info("👤 **Logged in as:** Priya Sharma\n\n📍 **Status:** Safe")

st.title("🗺️ AI Safe Route Recommendation")
st.caption("AI-powered routing that prioritizes your safety over shortest distance")

st.markdown("---")

col1, col2 = st.columns([1, 1])
with col1:
    origin = st.text_input("📍 Origin", placeholder="e.g. Rajouri Garden, Delhi")
with col2:
    destination = st.text_input("🏁 Destination", placeholder="e.g. Connaught Place, Delhi")

travel_time = st.selectbox("🕐 Travel Time", ["Now", "Tonight (after 8 PM)", "Late Night (after 11 PM)", "Early Morning (before 6 AM)"])
search = st.button("🔍 Find Safest Route", type="primary", use_container_width=True)

st.markdown("---")

m = folium.Map(location=[28.6139, 77.2090], zoom_start=13, tiles="CartoDB dark_matter")

safe_route = [
    [28.6010, 77.1950], [28.6040, 77.2000],
    [28.6080, 77.2050], [28.6139, 77.2090],
]
fast_route = [
    [28.6010, 77.1950], [28.6090, 77.1960],
    [28.6130, 77.2020], [28.6139, 77.2090],
]

folium.PolyLine(safe_route, weight=4, color="#00E676", opacity=0.9, tooltip="✅ Safest Route (Recommended)").add_to(m)
folium.PolyLine(fast_route, weight=3, color="#FF6B35", opacity=0.6, dash_array="10", tooltip="⚡ Fastest Route (Less Safe)").add_to(m)

folium.Marker([28.6010, 77.1950], icon=folium.Icon(color="green", icon="home", prefix="fa"), tooltip="Origin").add_to(m)
folium.Marker([28.6139, 77.2090], icon=folium.Icon(color="red", icon="flag", prefix="fa"), tooltip="Destination").add_to(m)

for loc, label in [([28.6055, 77.2025], "🏮 Well-lit area"), ([28.6100, 77.2060], "👮 Police patrol zone")]:
    folium.CircleMarker(loc, radius=8, color="#00E676", fill=True, fill_opacity=0.5, tooltip=label).add_to(m)

for loc, label in [([28.6090, 77.1975], "⚠️ Poorly lit"), ([28.6115, 77.1990], "⚠️ Low activity area")]:
    folium.CircleMarker(loc, radius=8, color="#FF6B35", fill=True, fill_opacity=0.5, tooltip=label).add_to(m)

st_folium(m, width="100%", height=400)

st.markdown("---")
r1, r2 = st.columns(2)

with r1:
    st.subheader("✅ Safest Route (Recommended)")
    st.success(
        "**Via: MG Road → Central Park → CP Inner Circle**\n\n"
        "📏 Distance: 8.7 km\n\n"
        "⏱ Duration: ~38 min\n\n"
        "🛡 Safety Score: **92 / 100**\n\n"
        "💡 Well-lit throughout · Police patrols · High footfall\n\n"
        "⚠️ Avoid: Underpass near Metro Gate 4 (poorly lit)"
    )

with r2:
    st.subheader("⚡ Fastest Route")
    st.warning(
        "**Via: Ring Road → Shortcut Lane → CP**\n\n"
        "📏 Distance: 7.1 km\n\n"
        "⏱ Duration: ~28 min\n\n"
        "🛡 Safety Score: **54 / 100**\n\n"
        "❌ Poorly lit sections · Isolated areas\n\n"
        "❌ Not recommended after 8 PM"
    )

st.markdown("---")
st.subheader("📊 Route Safety Analysis")
factors = pd.DataFrame({
    "Safety Factor": ["Street Lighting", "Police Presence", "Public Activity", "Crime History", "CCTV Coverage"],
    "Safe Route": [95, 85, 90, 88, 80],
    "Fast Route": [45, 30, 40, 35, 25],
})

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Bar(name="Safe Route", x=factors["Safety Factor"], y=factors["Safe Route"], marker_color="#00E676"))
fig.add_trace(go.Bar(name="Fast Route", x=factors["Safety Factor"], y=factors["Fast Route"], marker_color="#FF6B35"))
fig.update_layout(
    barmode="group", paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)", font_color="#FFFFFF",
    height=280, margin=dict(l=0, r=0, t=10, b=0),
)
st.plotly_chart(fig, use_container_width=True)
