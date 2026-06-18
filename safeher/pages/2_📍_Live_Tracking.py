import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import datetime
import random

st.set_page_config(page_title="Live Tracking – SafeHer AI", page_icon="📍", layout="wide")

st.sidebar.title("🛡 SafeHer AI")
st.sidebar.caption("Intelligent Women Safety System")
st.sidebar.markdown("---")
st.sidebar.info("👤 **Logged in as:** Priya Sharma\n\n📍 **Status:** Safe")

st.title("📍 Live Location Tracking")
st.caption("Real-time GPS tracking visible to your trusted contacts")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🗺️ Current Location Map")
    m = folium.Map(location=[28.6139, 77.2090], zoom_start=14, tiles="CartoDB dark_matter")

    folium.Marker(
        [28.6139, 77.2090],
        popup="📍 Priya's Current Location\nConnaught Place, Delhi",
        tooltip="You are here",
        icon=folium.Icon(color="red", icon="user", prefix="fa"),
    ).add_to(m)

    route_points = [
        [28.6010, 77.1950],
        [28.6050, 77.2000],
        [28.6100, 77.2040],
        [28.6139, 77.2090],
    ]
    folium.PolyLine(
        route_points,
        weight=3,
        color="#E91E8C",
        opacity=0.9,
        tooltip="Travel Route",
    ).add_to(m)

    folium.Marker(
        [28.6010, 77.1950],
        popup="🏠 Home – Journey started",
        tooltip="Journey Start",
        icon=folium.Icon(color="green", icon="home", prefix="fa"),
    ).add_to(m)

    folium.Marker(
        [28.6250, 77.2180],
        popup="🚔 Sector 10 Police Station\n📞 100",
        tooltip="Nearest Police Station",
        icon=folium.Icon(color="blue", icon="shield", prefix="fa"),
    ).add_to(m)

    folium.Circle(
        location=[28.6139, 77.2090],
        radius=300,
        color="#E91E8C",
        fill=True,
        fill_opacity=0.1,
        tooltip="Safety Zone",
    ).add_to(m)

    st_folium(m, width="100%", height=420)

with col2:
    st.subheader("📡 Tracking Status")
    st.metric("GPS Accuracy", "±5 meters", delta="High")
    st.metric("Speed", "12 km/h", delta="Moving")
    st.metric("Battery", "78%", delta="-2%")
    st.metric("Network", "4G LTE", delta="Strong")

    st.markdown("---")
    st.subheader("🛣️ Journey Details")
    st.markdown(
        "**Started:** 10:15 AM\n\n"
        "**Origin:** Home, Rajouri Garden\n\n"
        "**Destination:** Office, Connaught Place\n\n"
        "**Distance Covered:** 4.2 km\n\n"
        "**ETA:** 10:42 AM (in 8 min)\n\n"
        "**Route Safety:** 🟢 Safe"
    )

    st.markdown("---")
    st.subheader("👥 Shared With")
    for name in ["Mom", "Sister Priya", "Best Friend Riya"]:
        st.markdown(f"🟢 **{name}** — Watching live")

    st.markdown("---")
    tracking_active = st.toggle("Live Tracking Active", value=True)
    if tracking_active:
        st.success("✅ Your location is being shared live.")
    else:
        st.warning("⚠️ Live tracking is paused.")

st.markdown("---")
st.subheader("📅 Location History (Last 7 Days)")
history = pd.DataFrame({
    "Date": pd.date_range(end=datetime.date.today(), periods=7),
    "Start": ["Home", "Home", "Office", "Home", "Mall", "Home", "Home"],
    "End": ["Office", "Mall", "Home", "Hospital", "Home", "Gym", "Office"],
    "Distance": ["8.2 km", "5.4 km", "8.1 km", "3.0 km", "6.7 km", "2.1 km", "8.3 km"],
    "Safety": ["🟢 Safe", "🟢 Safe", "🟡 Caution", "🟢 Safe", "🟢 Safe", "🟢 Safe", "🟢 Safe"],
    "Duration": ["35 min", "22 min", "33 min", "15 min", "28 min", "12 min", "36 min"],
})
st.dataframe(history, use_container_width=True, hide_index=True)
