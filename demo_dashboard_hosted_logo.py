
import streamlit as st
import json
import os

st.set_page_config(page_title="CJX Aegis Demo", layout="wide")

# Hosted logo image (fallback)
logo_url = "https://raw.githubusercontent.com/cjxsecuresystems/cjx-demo-dashboard/main/assets/cjx_logo_transparent.png"
st.image(logo_url, width=120)
st.markdown("<h1 style='color: #003366;'>CJX Aegis - Cybersecurity Demo</h1>", unsafe_allow_html=True)

# Load scenarios
with open("scenarios.json", "r") as f:
    scenarios = json.load(f)["scenarios"]

# Scenario selection
titles = [s["title"] for s in scenarios]
selected = st.sidebar.selectbox("Choose a breach scenario", titles)
scenario = next(s for s in scenarios if s["title"] == selected)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Active Alerts", 4)
col2.metric("System Uptime", "98.62%")
col3.metric("Online Devices", 20)

st.markdown("### 🔍 Breach Summary")
st.subheader(f"{scenario['company']} — {scenario['title']}")
st.write(scenario["summary"])

st.markdown("### 🚨 Triggered Alerts")
st.code("\n".join(scenario["alerts"]))

st.markdown("### 🔥 Breach Impact")
st.info(scenario["impact"])

st.markdown("### 🛠️ CJX Response Plan")
st.success(scenario["action_plan"])

st.markdown("---")
st.subheader("🧠 Agent Response Controls")

if st.button("🚀 Deploy CJX Agent"):
    st.success("CJX Agent deployed. Threat neutralized and system secured.")

report_file = scenario.get("report_file")
if report_file and os.path.exists(report_file):
    with open(report_file, "rb") as f:
        st.download_button("📥 Download Incident Report", f, file_name=report_file, mime="application/pdf")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: gray;'>"
    "© 2025 CJX Secure Systems — All rights reserved. | <a href='https://www.cjxsecure.com'>www.cjxsecure.com</a>"
    "</p>", unsafe_allow_html=True)
