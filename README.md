
# 📍 Terminal Location Tracker

**Terminal Location Tracker** is a lightweight, fully terminal-based Python tool that lets you:

- 🌍 Find your **own public IP** and geolocation
- 🔍 Lookup any **other IP address** for location and ISP info
- 📡 Run a **minimal HTTP server** to receive live GPS coordinates
- 🧾 Log all received locations to a text file — no database required

> ⚙️ Built using only Python standard libraries — no Flask, no JavaScript!

---

## 🛠️ Built With

- **Language**: [Python 3.13.2](https://www.python.org/)
- **Libraries**: Only uses Python’s built-in modules:
  - `http.server`
  - `json`
  - `urllib.request`
  - `datetime`
  - `threading`

---

## 🚀 Features

- ✅ Terminal menu interface
- 🌐 Public IP & geolocation via `ipinfo.io`
- 📡 HTTP server to receive live GPS data
- 💾 All location data saved to `location_log.txt`
- 🐍 100% pure Python — no external dependencies

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/terminal-location-tracker.git
cd terminal-location-tracker
