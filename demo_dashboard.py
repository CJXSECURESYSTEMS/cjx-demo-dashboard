
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import datetime
import random
import os

DEMO_MODE = True

# Auto-refresh every 30s
st_autorefresh(interval=30000, key="demo_refresh")

# Red alert banner
if DEMO_MODE:
    st.markdown("""
    <div style='background-color:#e74c3c; padding:10px 15px; border-radius:6px; font-weight:bold; color:white; text-align:center;'>
    🚫 This is a DEMO. No actions will be executed.
    </div>
    """, unsafe_allow_html=True)

# Demo metrics
if DEMO_MODE:
    mock_data = {
        "alerts": random.randint(0, 5),
        "uptime": f"{round(random.uniform(98.0, 99.99), 2)}%",
        "devices_online": random.randint(5, 20)
    }

    st.metric("Active Alerts", mock_data["alerts"])
    st.metric("System Uptime", mock_data["uptime"])
    st.metric("Online Devices", mock_data["devices_online"])

# Disabled actions
st.divider()
st.subheader("Controls (Demo Locked)")

st.button("Deploy Agent", disabled=True)
st.button("Download Audit Report", disabled=True)
st.button("Export Logs", disabled=True)
st.caption("🔒 All controls are disabled in demo mode.")

# Log user intent
def log_action(action: str):
    with open("demo_audit_log.txt", "a") as log:
        log.write(f"[{datetime.datetime.now()}] Demo Action Attempt: {action}\n")

if st.button("Simulate Incident Alert"):
    log_action("Attempted incident simulation")
    st.warning("🚫 Action not allowed in demo.")

# Watermark
st.markdown("""
    <div style='position:fixed; bottom:10px; right:10px; 
    background-color:#f39c12; color:white; padding:5px 15px; 
    border-radius:8px; font-weight:bold;'>DEMO MODE</div>
""", unsafe_allow_html=True)
