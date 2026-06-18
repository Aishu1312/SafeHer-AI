import streamlit as st
import folium
from streamlit_folium import st_folium
from safeher.utils.helpers import get_nearby_places

st.set_page_config(page_title="Help Centers – SafeHer AI", page_icon="🏥", layout="wide")

st.sidebar.title("🛡 SafeHer AI")
st.sidebar.caption("Intelligent Women Safety System")
st.sidebar.markdown("---")
st.sidebar.info("👤 **Logged in as:** Priya Sharma\n\n📍 **Status:** Safe")

st.title("🏥 Nearby Help Centers")
st.caption("Police stations, hospitals, and women helplines near you — always updated in real time")

st.markdown("---")

filter_col1, filter_col2 = st.columns([2, 1])
with filter_col1:
    search_radius = st.slider("Search Radius (km)", 0.5, 10.0, 3.0, 0.5)
with filter_col2:
    sort_by = st.selectbox("Sort By", ["Distance", "Rating", "Open Now"])

places = get_nearby_places()

m = folium.Map(location=[28.6139, 77.2090], zoom_start=14, tiles="CartoDB dark_matter")

folium.Marker(
    [28.6139, 77.2090],
    popup="📍 Your Location",
    icon=folium.Icon(color="red", icon="user", prefix="fa"),
).add_to(m)

police_coords = [[28.6250, 77.2180], [28.6050, 77.2100], [28.6300, 77.1980]]
hospital_coords = [[28.6180, 77.2250], [28.6080, 77.1980], [28.6320, 77.2150]]

for (coord, p) in zip(police_coords, places["Police Stations"]):
    folium.Marker(
        coord,
        popup=f"🚔 {p['name']}\n📞 {p['phone']}\n📏 {p['distance']}",
        icon=folium.Icon(color="blue", icon="shield", prefix="fa"),
        tooltip=p["name"],
    ).add_to(m)

for (coord, h) in zip(hospital_coords, places["Hospitals"]):
    folium.Marker(
        coord,
        popup=f"🏥 {h['name']}\n📞 {h['phone']}\n📏 {h['distance']}",
        icon=folium.Icon(color="green", icon="plus-square", prefix="fa"),
        tooltip=h["name"],
    ).add_to(m)

folium.Circle(
    location=[28.6139, 77.2090],
    radius=search_radius * 1000,
    color="#E91E8C",
    fill=True,
    fill_opacity=0.05,
    tooltip=f"Search radius: {search_radius} km",
).add_to(m)

st_folium(m, width="100%", height=380)

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["🚔 Police Stations", "🏥 Hospitals", "📞 Women Helplines"])

with tab1:
    for p in places["Police Stations"]:
        with st.container():
            c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
            with c1:
                st.markdown(f"**🚔 {p['name']}**")
            with c2:
                st.markdown(f"📏 {p['distance']}")
            with c3:
                st.markdown(f"⏰ {p['open']}")
            with c4:
                if st.button(f"📞 {p['phone']}", key=f"police_{p['name']}"):
                    st.info(f"Calling {p['phone']}...")
            st.markdown("---")

with tab2:
    for h in places["Hospitals"]:
        with st.container():
            c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
            with c1:
                st.markdown(f"**🏥 {h['name']}**")
            with c2:
                st.markdown(f"📏 {h['distance']}")
            with c3:
                st.markdown(f"⏰ {h['open']}")
            with c4:
                if st.button(f"📞 {h['phone']}", key=f"hosp_{h['name']}"):
                    st.info(f"Calling {h['phone']}...")
            st.markdown("---")

with tab3:
    for w in places["Women Helplines"]:
        with st.container():
            c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
            with c1:
                st.markdown(f"**📞 {w['name']}**")
            with c2:
                st.markdown(f"📏 {w['distance']}")
            with c3:
                st.markdown(f"⏰ {w['open']}")
            with c4:
                if st.button(f"📞 {w['phone']}", key=f"help_{w['name']}"):
                    st.info(f"Calling {w['phone']}...")
            st.markdown("---")
