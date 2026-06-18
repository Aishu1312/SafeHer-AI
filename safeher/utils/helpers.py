import random
import datetime
import pandas as pd
import numpy as np


def get_mock_contacts():
    return [
        {"name": "Mom", "phone": "+91-98765-43210", "relation": "Mother"},
        {"name": "Sister Priya", "phone": "+91-91234-56789", "relation": "Sister"},
        {"name": "Best Friend Riya", "phone": "+91-87654-32109", "relation": "Friend"},
    ]


def get_mock_alerts():
    now = datetime.datetime.now()
    alerts = []
    for i in range(8):
        t = now - datetime.timedelta(hours=random.randint(1, 72))
        alerts.append({
            "Time": t.strftime("%d %b %Y, %I:%M %p"),
            "Type": random.choice(["SOS Triggered", "Voice Command", "Manual Alert", "Route Deviation"]),
            "Location": random.choice([
                "Connaught Place, Delhi",
                "MG Road, Bangalore",
                "Linking Road, Mumbai",
                "Park Street, Kolkata",
                "Jubilee Hills, Hyderabad",
            ]),
            "Risk Level": random.choice(["🔴 High", "🟡 Medium", "🟢 Low"]),
            "Status": random.choice(["Resolved", "Active", "Resolved", "Resolved"]),
        })
    return pd.DataFrame(alerts)


def get_risk_score(voice_input: str) -> int:
    danger_keywords = [
        "help", "danger", "emergency", "save me", "scared",
        "attack", "threat", "unsafe", "please help", "follow",
        "hurt", "chase", "stop", "leave me", "alone",
    ]
    text = voice_input.lower()
    hits = sum(1 for kw in danger_keywords if kw in text)
    base = min(hits * 22, 85)
    noise = random.randint(-5, 10)
    return max(5, min(100, base + noise))


def get_nearby_places():
    return {
        "Police Stations": [
            {"name": "Sector 10 Police Station", "distance": "0.8 km", "phone": "100", "open": "24/7"},
            {"name": "City Central Thana", "distance": "1.4 km", "phone": "011-23456789", "open": "24/7"},
            {"name": "Women Help Desk – North", "distance": "2.1 km", "phone": "1091", "open": "24/7"},
        ],
        "Hospitals": [
            {"name": "City General Hospital", "distance": "1.1 km", "phone": "102", "open": "24/7"},
            {"name": "Sunrise Medical Centre", "distance": "1.9 km", "phone": "011-98765432", "open": "24/7"},
            {"name": "Apollo Clinic", "distance": "2.6 km", "phone": "011-11223344", "open": "8am–10pm"},
        ],
        "Women Helplines": [
            {"name": "National Women Helpline", "distance": "—", "phone": "181", "open": "24/7"},
            {"name": "Police Emergency", "distance": "—", "phone": "100", "open": "24/7"},
            {"name": "Ambulance", "distance": "—", "phone": "102", "open": "24/7"},
        ],
    }


def generate_route_data():
    np.random.seed(42)
    waypoints = [
        (28.6139, 77.2090),
        (28.6200, 77.2150),
        (28.6280, 77.2220),
        (28.6350, 77.2300),
    ]
    return waypoints


def get_activity_data():
    dates = pd.date_range(end=datetime.date.today(), periods=30)
    data = pd.DataFrame({
        "Date": dates,
        "Trips": np.random.randint(1, 6, 30),
        "SOS Events": np.random.choice([0, 0, 0, 1], 30),
        "Risk Score": np.random.randint(10, 70, 30),
    })
    return data
