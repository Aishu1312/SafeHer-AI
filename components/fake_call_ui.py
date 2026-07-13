import streamlit.components.v1 as components
import base64

def render_fake_call(caller_name: str, voice_base64: str, ringtone_url: str):
    """
    Renders a realistic full-screen smartphone fake call interface using HTML/JS/CSS.
    It manages the entire audio and state sequence locally without triggering Streamlit reruns.
    """
    
    # If no custom ringtone is provided, use a modern default ringtone.
    if not ringtone_url:
        ringtone_url = "https://actions.google.com/sounds/v1/alarms/phone_ringing.ogg"
        
    # We pass the base64 audio string to the frontend if available.
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
                background: linear-gradient(135deg, #1f1f2e 0%, #0d0d14 100%);
                border-radius: 40px;
                border: 8px solid #2a2a35;
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
                padding: 10px 20px;
                box-sizing: border-box;
                font-size: 12px;
                opacity: 0.8;
            }}
            
            /* Caller Info */
            .caller-info {{
                margin-top: 40px;
                text-align: center;
            }}
            .caller-status {{
                font-size: 16px;
                color: #aaa;
                margin-bottom: 15px;
                font-weight: 300;
            }}
            .caller-name {{
                font-size: 32px;
                font-weight: 400;
                margin: 0;
            }}
            .caller-type {{
                font-size: 14px;
                color: #888;
                margin-top: 5px;
            }}
            
            /* Avatar */
            .avatar-container {{
                margin-top: 30px;
                position: relative;
            }}
            .avatar {{
                width: 120px;
                height: 120px;
                background-color: #555;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 60px;
                z-index: 2;
                position: relative;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            }}
            .ripple {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 120px;
                height: 120px;
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 50%;
                z-index: 1;
                animation: ripple-anim 2s infinite ease-out;
            }}
            @keyframes ripple-anim {{
                0% {{ width: 120px; height: 120px; opacity: 1; }}
                100% {{ width: 250px; height: 250px; opacity: 0; }}
            }}
            
            /* Actions */
            .actions-container {{
                position: absolute;
                bottom: 50px;
                width: 100%;
                display: flex;
                justify-content: space-around;
                padding: 0 40px;
                box-sizing: border-box;
            }}
            .action-btn {{
                display: flex;
                flex-direction: column;
                align-items: center;
                cursor: pointer;
            }}
            .btn-circle {{
                width: 70px;
                height: 70px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 30px;
                color: white;
                border: none;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                transition: transform 0.2s;
            }}
            .btn-circle:hover {{
                transform: scale(1.05);
            }}
            .btn-decline {{ background-color: #FF3B30; }}
            .btn-accept {{ background-color: #34C759; animation: bounce 2s infinite; }}
            
            @keyframes bounce {{
                0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
                40% {{ transform: translateY(-10px); }}
                60% {{ transform: translateY(-5px); }}
            }}
            
            .btn-label {{
                margin-top: 10px;
                font-size: 14px;
                color: #ccc;
            }}
            
            /* Timer */
            .timer {{
                font-size: 18px;
                color: #34C759;
                margin-top: 15px;
                display: none;
            }}
            
            /* In-Call Controls */
            .incall-controls {{
                position: absolute;
                bottom: 160px;
                width: 100%;
                display: flex;
                flex-wrap: wrap;
                justify-content: space-evenly;
                gap: 20px;
                display: none;
                padding: 0 30px;
                box-sizing: border-box;
            }}
            .incall-btn {{
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background-color: rgba(255, 255, 255, 0.15);
                border: none;
                color: white;
                font-size: 24px;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
        </style>
    </head>
    <body>
        <div class="phone-container" id="phone">
            <div class="status-bar">
                <span>12:00</span>
                <span>LTE 🔋</span>
            </div>
            
            <div class="caller-info">
                <div class="caller-status" id="status-text">Incoming Call</div>
                <h1 class="caller-name">{caller_name}</h1>
                <div class="caller-type" id="caller-type">Mobile</div>
                <div class="timer" id="timer">00:00</div>
            </div>
            
            <div class="avatar-container" id="avatar-container">
                <div class="ripple" id="ripple"></div>
                <div class="avatar">👤</div>
            </div>
            
            <div class="incall-controls" id="incall-controls">
                <button class="incall-btn">🔇</button>
                <button class="incall-btn">⏺️</button>
                <button class="incall-btn">🔈</button>
                <button class="incall-btn">⏸️</button>
            </div>
            
            <div class="actions-container" id="actions">
                <div class="action-btn" onclick="declineCall()" id="btn-decline">
                    <button class="btn-circle btn-decline">☎️</button>
                    <div class="btn-label">Decline</div>
                </div>
                <div class="action-btn" onclick="acceptCall()" id="btn-accept">
                    <button class="btn-circle btn-accept">📞</button>
                    <div class="btn-label">Accept</div>
                </div>
            </div>
            
            <!-- End Call Container (Hidden initially) -->
            <div class="actions-container" id="end-action" style="display: none; justify-content: center;">
                <div class="action-btn" onclick="endCall()">
                    <button class="btn-circle btn-decline">☎️</button>
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
            let ringtone = document.getElementById("ringtone");
            let voiceMsg = document.getElementById("voice-message");
            let timerInterval;
            let ringtoneInterval;
            let seconds = 0;
            
            // Start ringtone immediately 
            ringtone.play().catch(e => console.log("Autoplay blocked, waiting for interaction"));
            
            // Create a natural pause loop for the ringtone
            ringtone.addEventListener('ended', function() {{
                // When audio ends, wait 2 seconds before playing again to simulate real phone ring
                ringtoneInterval = setTimeout(() => {{
                    ringtone.play().catch(e => {{}});
                }}, 2000);
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
                
                document.getElementById("btn-decline").style.display = "none";
                document.getElementById("btn-accept").style.display = "none";
                document.getElementById("end-action").style.display = "flex";
                
                document.getElementById("status-text").style.display = "none";
                document.getElementById("caller-type").style.display = "none";
                document.getElementById("ripple").style.display = "none";
                
                let timerEl = document.getElementById("timer");
                timerEl.style.display = "block";
                
                document.getElementById("incall-controls").style.display = "flex";
                document.getElementById("avatar-container").style.transform = "scale(0.8)";
                document.getElementById("avatar-container").style.transition = "transform 0.5s ease";

                // Start Timer
                timerInterval = setInterval(() => {{
                    seconds++;
                    timerEl.innerText = formatTime(seconds);
                }}, 1000);
                
                // Play Voice Message
                if ("{voice_src}" !== "") {{
                    voiceMsg.play();
                }}
            }}

            function declineCall() {{
                endCallLogic("Call Declined");
            }}

            function endCall() {{
                endCallLogic("Call Ended");
            }}
            
            function endCallLogic(msg) {{
                clearTimeout(ringtoneInterval);
                ringtone.pause();
                voiceMsg.pause();
                clearInterval(timerInterval);
                
                document.getElementById("timer").style.display = "none";
                document.getElementById("status-text").innerText = msg;
                document.getElementById("status-text").style.display = "block";
                
                document.getElementById("actions").style.display = "none";
                document.getElementById("end-action").style.display = "none";
                document.getElementById("incall-controls").style.display = "none";
                document.getElementById("ripple").style.display = "none";
                
                document.getElementById("phone").style.opacity = "0.5";
            }}
        </script>
    </body>
    </html>
    """
    
    components.html(html_content, height=620)
