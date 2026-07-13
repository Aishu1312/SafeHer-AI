import streamlit as st
import time
from styles.css import inject_custom_css

st.set_page_config(page_title="Fake Call - SafeHer AI", page_icon="📞", layout="wide")
inject_custom_css()

st.title("📞 Fake Call Generator")
st.caption("Escape uncomfortable situations with a simulated incoming call")
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("⚙️ Call Settings")
    
    caller_name = st.text_input("Caller Name", value="Mom")
    delay = st.selectbox("Trigger Delay", ["Immediately", "15 seconds", "30 seconds", "1 minute", "5 minutes"])
    voice_msg = st.selectbox(
        "Voice on Answer", 
        ["Where are you? Come home right now!", "Hey, I'm waiting outside for you.", "Emergency! Can you pick up the call?"]
    )
    
    delay_map = {
        "Immediately": 0,
        "15 seconds": 15,
        "30 seconds": 30,
        "1 minute": 60,
        "5 minutes": 300
    }
    
    if st.button("🚨 Schedule Fake Call", type="primary", use_container_width=True):
        st.session_state.fake_call_triggered = True
        st.session_state.fake_call_time = time.time() + delay_map[delay]
        st.session_state.fake_call_caller = caller_name
        st.success(f"Fake call from {caller_name} scheduled!")
        
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("📱 Call Status")
    
    if st.session_state.get('fake_call_triggered', False):
        time_left = st.session_state.fake_call_time - time.time()
        if time_left > 0:
            st.info(f"⏳ Call incoming in {int(time_left)} seconds...")
            time.sleep(1)
            st.rerun()
        else:
            # Simulate Incoming Call UI
            caller = st.session_state.get('fake_call_caller', 'Mom')
            import streamlit.components.v1 as components
            components.html(f"""
            <div style="background-color: #1c1c1e; border-radius: 30px; padding: 40px 20px; text-align: center; border: 2px solid #333; max-width: 350px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.5); font-family: sans-serif;">
                <h4 style="color: #aaa; margin: 0; font-weight: normal;">Incoming call...</h4>
                <div style="width: 80px; height: 80px; background-color: #555; border-radius: 50%; margin: 20px auto; display: flex; align-items: center; justify-content: center; font-size: 40px;">
                    👤
                </div>
                <h1 style="color: white; margin: 10px 0;">{caller}</h1>
                <p style="color: #aaa; margin-bottom: 40px;">Mobile</p>
                
                <div style="display: flex; justify-content: space-around; margin-top: 20px;">
                    <div style="text-align: center;">
                        <button onclick="alert('Call Rejected')" style="width: 65px; height: 65px; border-radius: 50%; background-color: #FF3B30; border: none; color: white; font-size: 30px; cursor: pointer; box-shadow: 0 4px 10px rgba(255,59,48,0.4);">
                            ☎️
                        </button>
                        <p style="color: white; margin-top: 10px; font-size: 14px;">Decline</p>
                    </div>
                    <div style="text-align: center;">
                        <button onclick="document.getElementById('fake-audio').play(); this.innerHTML='Talking...'; this.style.backgroundColor='#555';" style="width: 65px; height: 65px; border-radius: 50%; background-color: #34C759; border: none; color: white; font-size: 30px; cursor: pointer; box-shadow: 0 4px 10px rgba(52,199,89,0.4);">
                            📞
                        </button>
                        <p style="color: white; margin-top: 10px; font-size: 14px;">Accept</p>
                    </div>
                </div>
                
                <!-- Hidden Audio Element -->
                <audio id="fake-audio" src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg"></audio>
            </div>
            """, height=450)
            
            if st.button("Reset Call"):
                st.session_state.fake_call_triggered = False
                st.rerun()
    else:
        st.markdown("""
        <div style="text-align: center; padding: 40px 0; color: #aaa;">
            <p style="font-size: 50px; margin: 0;">📱</p>
            <p>No active fake calls.</p>
            <p>Schedule one from the settings panel.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
