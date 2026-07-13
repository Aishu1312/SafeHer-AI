import streamlit as st
import time
import urllib.parse
from styles.css import inject_custom_css
from localization.manager import _

st.set_page_config(page_title=_("Help Centers") + " - SafeHer AI", page_icon="🏥", layout="wide")
inject_custom_css()

st.title(f"🏥 {_('Nearby Help Centers')}")
st.caption(_("Find and navigate to police stations, hospitals, and women helplines instantly"))
st.markdown("---")

lat = st.session_state.user['location'].get('lat')
lon = st.session_state.user['location'].get('lon')

if not lat:
    st.warning(_("⚠️ Location not found! Please go to the 'Live Location' tab to fetch your current location."))
    # Fallback to general search without location context
    lat, lon = "28.6139", "77.2090" # Default Delhi

col1, col2 = st.columns([1, 1])

def create_place_card(title, query, icon, description, phone="100"):
    encoded_query = urllib.parse.quote(query)
    maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_query}"
    
    html = f"""
    <div class="glass-card" style="margin-bottom: 15px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
                <h3 style="margin: 0; padding: 0;">{icon} {title}</h3>
                <p style="color: #ccc; font-size: 14px; margin: 5px 0;">{description}</p>
                <p style="color: #E91E8C; font-weight: bold; margin: 0;">📞 {phone}</p>
            </div>
        </div>
        <div style="display: flex; gap: 10px; margin-top: 15px; flex-wrap: wrap;">
            <a href="{maps_url}" target="_blank" style="text-decoration: none; flex: 1;">
                <button style="width: 100%; background: rgba(255,255,255,0.1); border: 1px solid #E91E8C; border-radius: 8px; color: white; padding: 8px; cursor: pointer;">
                    🗺️ {_('Open in Google Maps')}
                </button>
            </a>
            <a href="tel:{phone}" style="text-decoration: none; flex: 1;">
                <button style="width: 100%; background: #E91E8C; border: none; border-radius: 8px; color: white; padding: 8px; font-weight: bold; cursor: pointer;">
                    📞 {_('Call Now')}
                </button>
            </a>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

with col1:
    st.subheader(f"🚔 {_('Emergency & Police')}")
    create_place_card(_("Nearby Police Stations"), _("police stations near me"), "🚔", _("Find the closest local police station for immediate help."), "100")
    create_place_card(_("Women Police Stations"), _("women police stations near me"), "🛡️", _("Specialized police stations for women's safety."), "1091")
    create_place_card(_("Emergency Shelters"), _("women emergency shelters near me"), "🏠", _("Safe havens and temporary shelters."), "181")

with col2:
    st.subheader(f"🏥 {_('Medical & Support')}")
    create_place_card(_("Nearby Hospitals"), _("hospitals near me"), "🏥", _("General hospitals for medical emergencies."), "102")
    create_place_card(_("Emergency Clinics"), _("emergency clinics near me"), "⚕️", _("24/7 immediate medical care centers."), "108")
    create_place_card(_("Women NGOs"), _("women empowerment NGOs near me"), "🤝", _("Non-governmental organizations supporting women."), "181")

st.markdown("---")
st.info(f"💡 **{_('Tip')}:** {_('Google Maps links will automatically open in your Maps app on mobile devices, providing real-time directions based on your GPS.')}")
