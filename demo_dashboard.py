
import streamlit as st
import json
import datetime
import random
import os

st.set_page_config(page_title="CJX Aegis Demo", layout="wide")
st.image("assets/cjx_logo_transparent.png", width=180)

with open("scenarios.json", "r") as f:
    scenarios = json.load(f)["scenarios"]

st.sidebar.header("CJX Scenario Viewer")
scenario_options = [s["title"] for s in scenarios]
selected_title = st.sidebar.selectbox("Choose a breach scenario", scenario_options)

scenario = next(s for s in scenarios if s["title"] == selected_title)

st.title("🔒 CJX Aegis - Cybersecurity Incident Demo")

st.markdown("""
    <div style='background-color:#e74c3c; padding:10px 15px; border-radius:6px; font-weight:bold; color:white; text-align:center;'>
    🚫 This is a DEMO. No actions will be executed.
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Active Alerts", random.randint(2, 5))
col2.metric("System Uptime", f"{round(random.uniform(98.0, 99.99), 2)}%")
col3.metric("Online Devices", random.randint(10, 20))

st.markdown("---")
st.subheader(f"📌 {scenario['company']} - {scenario['title']}")
st.write(scenario["summary"])
st.write("### Triggered Alerts")
st.code("\n".join(scenario["alerts"]), language="bash")

st.write("### Breach Impact")
st.warning(scenario["impact"])

st.markdown("---")
st.subheader("Controls (Interactive Demo)")

if st.button("🚀 Deploy Agent"):
    st.success("Agent successfully simulated on target device!")

if st.button("📥 Download Audit Report"):
    if "AlphaTech" in scenario["company"]:
        with open("AlphaTech_Audit_Report.pdf", "rb") as f:
            st.download_button("Click to download AlphaTech Report", f, file_name="AlphaTech_Audit_Report.pdf")
    else:
        with open("BetaCorp_Audit_Report.pdf", "rb") as f:
            st.download_button("Click to download BetaCorp Report", f, file_name="BetaCorp_Audit_Report.pdf")

if st.button("🚨 Simulate Incident Alert"):
    st.warning("🚨 New incident alert triggered in mock log.")
