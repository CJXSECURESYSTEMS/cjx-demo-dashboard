
# CJX Aegis - Demo Mode Streamlit Template

This demo mode disables all write/export actions, auto-refreshes with mock data,
and logs all user interaction attempts without modifying backend systems.

## Features
- Auto-refresh every 30s
- Disabled export/download
- Mock metrics (alerts, uptime)
- Red "Demo Mode" warning banner
- Action audit log

## To Run
Install dependencies:
```
pip install streamlit streamlit-autorefresh
```

Start the demo dashboard:
```
streamlit run demo_dashboard.py
```

All attempts will be logged to `demo_audit_log.txt`.
