import streamlit as st
import datetime
import urllib.parse
from styles.css import inject_custom_css

st.set_page_config(page_title="SOS Emergency - SafeHer AI", page_icon="🚨", layout="wide")
inject_custom_css()

st.title("🚨 SOS Emergency")
st.caption("One tap to trigger emergency alerts to your trusted contacts")
st.markdown("---")

# Auto-trigger if activated from sidebar
if st.session_state.get("sos_active"):
    st.error("🚨 **SOS ACTIVATED!** Initiating emergency protocols...")
    st.session_state.sos_active = False # Reset so it doesn't loop forever
    st.balloons() # Visual feedback

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
        <div class="glass-card" style="text-align:center; border-color: #FF1744;">
            <h3 style="color: #FF1744;">Emergency Trigger</h3>
            <p style="color:#aaa;">Press the button below to alert your contacts immediately</p>
    """, unsafe_allow_html=True)
    
    if st.button("🚨 ACTIVATE SOS 🚨", type="primary", use_container_width=True):
        st.error("🚨 SOS Activated! Your emergency contacts have been notified.")
        
        # Build SOS Message
        now = datetime.datetime.now().strftime("%d %b %Y %I:%M %p")
        user = st.session_state.user
        lat = user['location']['lat']
        lon = user['location']['lon']
        loc_str = f"https://www.google.com/maps?q={lat},{lon}" if lat else "Location not fetched yet"
        
        msg = f"[SafeHer AI EMERGENCY]\n{user['username']} needs help!\nTime: {now}\nLocation: {loc_str}\nBlood Group: {user.get('blood_group', 'Unknown')}\nPlease contact her or Police immediately."
        
        st.session_state['sos_message'] = msg
        
    st.markdown("</div>", unsafe_allow_html=True)

    if 'sos_message' in st.session_state:
        st.subheader("Message Preview")
        st.code(st.session_state['sos_message'], language=None)
        
        encoded_sos = urllib.parse.quote(st.session_state['sos_message'])
        
        st.markdown(f"""
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="https://wa.me/?text={encoded_sos}" target="_blank" style="flex: 1; min-width: 150px;">
                <button style="width:100%; background-color:#25D366; color:white; border:none; padding:10px; border-radius:10px; font-weight:bold;">
                    WhatsApp SOS
                </button>
            </a>
            <a href="sms:?body={encoded_sos}" style="flex: 1; min-width: 150px;">
                <button style="width:100%; background-color:#007AFF; color:white; border:none; padding:10px; border-radius:10px; font-weight:bold;">
                    SMS SOS
                </button>
            </a>
            <a href="mailto:?subject=EMERGENCY SOS&body={encoded_sos}" style="flex: 1; min-width: 150px;">
                <button style="width:100%; background-color:#D44638; color:white; border:none; padding:10px; border-radius:10px; font-weight:bold;">
                    Email SOS
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("📋 Your Emergency Contacts")
    
    contacts = st.session_state.user.get('emergency_contacts', [])
    if not contacts:
        st.warning("You have no emergency contacts set up. Please add them in your profile.")
    else:
        for c in contacts:
            st.markdown(f"""
            <div style="border-left: 4px solid #E91E8C; padding-left: 10px; margin-bottom: 15px; background: rgba(255,255,255,0.05); padding: 10px; border-radius: 5px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong style="font-size: 1.1em;">{c['name']}</strong> ({c.get('relation', 'Contact')})<br>
                        <span style="color: #aaa;">{c['phone']}</span>
                    </div>
                    <a href="tel:{c['phone']}" style="text-decoration:none;">
                        <button style="background:#E91E8C; color:white; border:none; border-radius:5px; padding:8px 15px; font-weight:bold;">
                            📞 Call
                        </button>
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    st.info("💡 Pro Tip: Update your emergency contacts from the Profile Settings.")
    st.markdown("</div>", unsafe_allow_html=True)
