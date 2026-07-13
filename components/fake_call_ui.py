import streamlit.components.v1 as components
import base64

def render_fake_call(caller_name: str, voice_base64: str, ringtone_url: str, lang_data: dict = None):
    """
    Renders a realistic full-screen smartphone fake call interface using HTML/JS/CSS.
    Supports localized strings via lang_data.
    """
    if lang_data is None:
        lang_data = {
            "incoming": "Incoming Call",
            "mobile": "Mobile",
            "accept": "Accept",
            "decline": "Decline",
            "ended": "Call Ended",
            "declined": "Call Declined"
        }
    
    if not ringtone_url:
        ringtone_url = "https://actions.google.com/sounds/v1/alarms/phone_ringing.ogg"
        
    voice_src = f"data:audio/mp3;base64,{voice_base64}" if voice_base64 else ""

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: transparent;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 600px;
                color: white;
            }}
            .phone-container {{
                width: 360px;
                height: 600px;
                background: linear-gradient(135deg, #111116 0%, #050508 100%);
                border-radius: 40px;
                border: 10px solid #222;
                box-shadow: 0 20px 50px rgba(0,0,0,0.8);
                position: relative;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            
            /* Status Bar Fake */
            .status-bar {{
                width: 100%;
                height: 30px;
                display: flex;
                justify-content: space-between;
                padding: 10px 25px;
                box-sizing: border-box;
                font-size: 13px;
                font-weight: 500;
                opacity: 0.9;
            }}
            .status-icons span {{ margin-left: 5px; }}
            
            /* Caller Info */
            .caller-info {{
                margin-top: 35px;
                text-align: center;
            }}
            .caller-status {{
                font-size: 16px;
                color: #ccc;
                margin-bottom: 10px;
                font-weight: 400;
                letter-spacing: 1px;
            }}
            .caller-name {{
                font-size: 34px;
                font-weight: 300;
                margin: 0;
                text-shadow: 0 2px 10px rgba(0,0,0,0.5);
            }}
            .caller-type {{
                font-size: 15px;
                color: #888;
                margin-top: 8px;
            }}
            
            /* Avatar */
            .avatar-container {{
                margin-top: 40px;
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .avatar {{
                width: 130px;
                height: 130px;
                background: linear-gradient(45deg, #444, #666);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 65px;
                z-index: 2;
                position: relative;
                box-shadow: 0 10px 25px rgba(0,0,0,0.5);
                border: 2px solid rgba(255,255,255,0.1);
            }}
            
            /* Live Audio Waveform (Hidden until connected) */
            .waveform {{
                display: none;
                align-items: center;
                justify-content: center;
                gap: 5px;
                height: 40px;
                margin-top: 20px;
            }}
            .bar {{
                width: 6px;
                height: 10px;
                background-color: #34C759;
                border-radius: 3px;
                animation: wave 1s ease-in-out infinite alternate;
            }}
            .bar:nth-child(2) {{ animation-delay: -0.2s; }}
            .bar:nth-child(3) {{ animation-delay: -0.4s; }}
            .bar:nth-child(4) {{ animation-delay: -0.6s; }}
            .bar:nth-child(5) {{ animation-delay: -0.8s; }}
            
            @keyframes wave {{
                0% {{ height: 10px; opacity: 0.5; }}
                100% {{ height: 35px; opacity: 1; }}
            }}
            
            /* Ringing Ripple */
            .ripple {{
                position: absolute;
                width: 130px;
                height: 130px;
                background-color: rgba(255, 255, 255, 0.15);
                border-radius: 50%;
                z-index: 1;
                animation: ripple-anim 2s infinite cubic-bezier(0.4, 0, 0.2, 1);
            }}
            @keyframes ripple-anim {{
                0% {{ transform: scale(1); opacity: 1; }}
                100% {{ transform: scale(2.2); opacity: 0; }}
            }}
            
            /* Actions */
            .actions-container {{
                position: absolute;
                bottom: 60px;
                width: 100%;
                display: flex;
                justify-content: space-around;
                padding: 0 45px;
                box-sizing: border-box;
            }}
            .action-btn {{
                display: flex;
                flex-direction: column;
                align-items: center;
                cursor: pointer;
            }}
            .btn-circle {{
                width: 75px;
                height: 75px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 32px;
                color: white;
                border: none;
                box-shadow: 0 10px 20px rgba(0,0,0,0.4);
                transition: transform 0.2s;
            }}
            .btn-circle:hover {{
                transform: scale(1.05);
            }}
            .btn-decline {{ background-color: #FF3B30; }}
            .btn-accept {{ 
                background-color: #34C759; 
                animation: pulse 2s infinite; 
                box-shadow: 0 0 15px rgba(52,199,89,0.5);
            }}
            
            @keyframes pulse {{
                0% {{ transform: scale(1); box-shadow: 0 0 15px rgba(52,199,89,0.5); }}
                50% {{ transform: scale(1.05); box-shadow: 0 0 25px rgba(52,199,89,0.8); }}
                100% {{ transform: scale(1); box-shadow: 0 0 15px rgba(52,199,89,0.5); }}
            }}
            
            .btn-label {{
                margin-top: 12px;
                font-size: 15px;
                color: #ddd;
                font-weight: 400;
            }}
            
            /* Timer */
            .timer {{
                font-size: 20px;
                color: #34C759;
                margin-top: 15px;
                display: none;
                font-variant-numeric: tabular-nums;
            }}
            
            /* Blur overlay for background */
            .blur-bg {{
                position: absolute;
                top: 0; left: 0; right: 0; bottom: 0;
                background: radial-gradient(circle at center, rgba(52,199,89,0.1) 0%, rgba(0,0,0,0) 70%);
                z-index: 0;
            }}
            
            .content-z {{ z-index: 10; position: relative; width: 100%; display: flex; flex-direction: column; align-items: center; }}
            
        </style>
    </head>
    <body>
        <div class="phone-container" id="phone">
            <div class="blur-bg"></div>
            <div class="content-z">
                <div class="status-bar">
                    <span id="clock">12:00</span>
                    <span class="status-icons">📶 LTE 🔋</span>
                </div>
                
                <div class="caller-info">
                    <div class="caller-status" id="status-text">{lang_data['incoming']}</div>
                    <h1 class="caller-name">{caller_name}</h1>
                    <div class="caller-type" id="caller-type">{lang_data['mobile']}</div>
                    <div class="timer" id="timer">00:00</div>
                    <div class="waveform" id="waveform">
                        <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                    </div>
                </div>
                
                <div class="avatar-container" id="avatar-container">
                    <div class="ripple" id="ripple"></div>
                    <div class="avatar">👤</div>
                </div>
                
                <div class="actions-container" id="actions">
                    <div class="action-btn" onclick="declineCall()" id="btn-decline">
                        <button class="btn-circle btn-decline">☎️</button>
                        <div class="btn-label">{lang_data['decline']}</div>
                    </div>
                    <div class="action-btn" onclick="acceptCall()" id="btn-accept">
                        <button class="btn-circle btn-accept">📞</button>
                        <div class="btn-label">{lang_data['accept']}</div>
                    </div>
                </div>
                
                <div class="actions-container" id="end-action" style="display: none; justify-content: center;">
                    <div class="action-btn" onclick="endCall()">
                        <button class="btn-circle btn-decline" style="width:85px; height:85px; font-size:38px;">☎️</button>
                    </div>
                </div>
            </div>
        </div>

        <audio id="ringtone">
            <source src="{ringtone_url}" type="audio/ogg">
            <source src="{ringtone_url}" type="audio/mp3">
        </audio>
        
        <audio id="voice-message">
            <source src="{voice_src}" type="audio/mp3">
        </audio>

        <script>
            // Set live clock
            setInterval(() => {{
                let d = new Date();
                document.getElementById('clock').innerText = 
                    (d.getHours()%12 || 12) + ":" + (d.getMinutes()<10?'0':'') + d.getMinutes();
            }}, 1000);

            let ringtone = document.getElementById("ringtone");
            let voiceMsg = document.getElementById("voice-message");
            let timerInterval;
            let ringtoneInterval;
            let seconds = 0;
            
            ringtone.play().catch(e => console.log("Autoplay blocked"));
            
            ringtone.addEventListener('ended', function() {{
                ringtoneInterval = setTimeout(() => {{
                    ringtone.play().catch(e => {{}});
                }}, 2000);
            }});

            // When voice message finishes, stop waveform
            voiceMsg.addEventListener('ended', function() {{
                document.getElementById("waveform").style.display = "none";
            }});

            function formatTime(sec) {{
                let min = Math.floor(sec / 60);
                let s = sec % 60;
                return (min < 10 ? "0" + min : min) + ":" + (s < 10 ? "0" + s : s);
            }}

            function acceptCall() {{
                clearTimeout(ringtoneInterval);
                ringtone.pause();
                ringtone.currentTime = 0;
                
                document.getElementById("actions").style.display = "none";
                document.getElementById("end-action").style.display = "flex";
                
                document.getElementById("status-text").style.display = "none";
                document.getElementById("caller-type").style.display = "none";
                document.getElementById("ripple").style.display = "none";
                
                let timerEl = document.getElementById("timer");
                timerEl.style.display = "block";
                
                document.getElementById("avatar-container").style.transform = "scale(0.85)";
                document.getElementById("avatar-container").style.transition = "transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1)";
                document.getElementById("avatar-container").style.marginTop = "20px";

                timerInterval = setInterval(() => {{
                    seconds++;
                    timerEl.innerText = formatTime(seconds);
                }}, 1000);
                
                if ("{voice_src}" !== "") {{
                    voiceMsg.play();
                    document.getElementById("waveform").style.display = "flex";
                }}
            }}

            function declineCall() {{
                endCallLogic("{lang_data['declined']}");
            }}

            function endCall() {{
                endCallLogic("{lang_data['ended']}");
            }}
            
            function endCallLogic(msg) {{
                clearTimeout(ringtoneInterval);
                ringtone.pause();
                voiceMsg.pause();
                clearInterval(timerInterval);
                
                document.getElementById("timer").style.display = "none";
                document.getElementById("waveform").style.display = "none";
                document.getElementById("status-text").innerText = msg;
                document.getElementById("status-text").style.display = "block";
                document.getElementById("status-text").style.color = "#FF3B30";
                
                document.getElementById("actions").style.display = "none";
                document.getElementById("end-action").style.display = "none";
                document.getElementById("ripple").style.display = "none";
                
                document.getElementById("phone").style.opacity = "0.7";
                document.getElementById("phone").style.filter = "grayscale(100%)";
            }}
        </script>
    </body>
    </html>
    """
    
    components.html(html_content, height=620)
