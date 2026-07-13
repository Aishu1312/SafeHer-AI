import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation
from geopy.geocoders import Nominatim
import urllib.parse
from styles.css import inject_custom_css

st.set_page_config(page_title="Live Location - SafeHer AI", page_icon="📍", layout="wide")
inject_custom_css()

st.title("📍 Live Location Tracking")
st.caption("Share your exact location with trusted contacts")
st.markdown("---")

@st.cache_resource
def get_geocoder():
    return Nominatim(user_agent="SafeHer_AI_App")

def get_address(lat, lon):
    try:
        geo = get_geocoder()
        location = geo.reverse((lat, lon), exactly_one=True)
        return location.address if location else "Address not found"
    except Exception as e:
        return f"Could not fetch address: {e}"

st.markdown("### Get Your Current Location")
loc = streamlit_geolocation()

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    if loc and loc.get('latitude') and loc.get('longitude'):
        lat = loc['latitude']
        lon = loc['longitude']
        
        # Save to session state
        st.session_state.user['location']['lat'] = lat
        st.session_state.user['location']['lon'] = lon
        
        st.success(f"Location Found: {lat:.6f}, {lon:.6f}")
        
        # Fetch Address
        with st.spinner("Fetching address..."):
            address = get_address(lat, lon)
            st.session_state.user['location']['address'] = address
            st.markdown(f"**📍 Current Address:** {address}")
        
        # Map Display
        m = folium.Map(location=[lat, lon], zoom_start=15, tiles="CartoDB dark_matter")
        folium.Marker(
            [lat, lon],
            popup="You are here",
            icon=folium.Icon(color="red", icon="user", prefix="fa"),
        ).add_to(m)
        folium.Circle(
            location=[lat, lon],
            radius=150,
            color="#E91E8C",
            fill=True,
            fill_opacity=0.2
        ).add_to(m)
        st_folium(m, width="100%", height=400)
    else:
        st.info("Click the button above to allow GPS access and find your location.")
        # Fallback to Delhi if no location
        m = folium.Map(location=[28.6139, 77.2090], zoom_start=12, tiles="CartoDB dark_matter")
        st_folium(m, width="100%", height=400)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("🔗 Share Location")
    
    if st.session_state.user['location']['lat']:
        lat = st.session_state.user['location']['lat']
        lon = st.session_state.user['location']['lon']
        maps_link = f"https://www.google.com/maps?q={lat},{lon}"
        
        st.code(maps_link, language=None)
        
        message = f"Please track my live location. I am at: {maps_link}"
        encoded_message = urllib.parse.quote(message)
        
        st.markdown(f"""
        <a href="https://wa.me/?text={encoded_message}" target="_blank" style="text-decoration:none;">
            <button style="width:100%; background-color:#25D366; color:white; border:none; padding:10px; border-radius:10px; margin-bottom:10px; font-weight:bold;">
                🟢 Share via WhatsApp
            </button>
        </a>
        <a href="sms:?body={encoded_message}" style="text-decoration:none;">
            <button style="width:100%; background-color:#007AFF; color:white; border:none; padding:10px; border-radius:10px; margin-bottom:10px; font-weight:bold;">
                💬 Share via SMS
            </button>
        </a>
        """, unsafe_allow_html=True)
    else:
        st.warning("Fetch your location first to enable sharing.")
    
    st.markdown("</div>", unsafe_allow_html=True)
