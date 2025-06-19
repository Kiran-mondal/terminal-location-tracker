import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import json
from datetime import datetime

LOG_FILE = "location_log.txt"

# ===== SERVER TO RECEIVE LOCATION =====
class LocationReceiver(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/location':
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)
            try:
                payload = json.loads(data.decode())
                lat = payload.get("latitude")
                lon = payload.get("longitude")
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log = f"[{time}] Received -> Latitude: {lat}, Longitude: {lon}\n"
                print(log.strip())
                with open(LOG_FILE, "a") as f:
                    f.write(log)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"status": "Location logged"}')
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(f"Error: {str(e)}".encode())

def start_server():
    server = HTTPServer(('', 8080), LocationReceiver)
    print("[*] Location server started on port 8080...")
    server.serve_forever()

# ===== IP LOOKUP TOOL =====
def get_ip_info(ip=""):
    try:
        if not ip:
            url = "https://ipinfo.io/json"
        else:
            url = f"https://ipinfo.io/{ip}/json"
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            return data
    except Exception as e:
        return {"error": str(e)}

# ===== MAIN MENU LOOP =====
def menu():
    while True:
        print("\n=== Live Location & IP Finder ===")
        print("1. Get your public IP and location")
        print("2. Lookup another IP address")
        print("3. Start location receiver server")
        print("4. View location log")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            data = get_ip_info()
            if "error" in data:
                print("❌ Error:", data["error"])
            else:
                print(f"🌍 Your IP: {data.get('ip')}")
                print(f"📍 Location: {data.get('city')}, {data.get('region')}, {data.get('country')}")
                print(f"🌐 ISP: {data.get('org')}")
                print(f"🗺️ Coordinates: {data.get('loc')}")
        elif choice == "2":
            ip = input("Enter target IP address: ")
            data = get_ip_info(ip)
            if "error" in data:
                print("❌ Error:", data["error"])
            else:
                print(f"🔍 IP: {data.get('ip')}")
                print(f"📍 Location: {data.get('city')}, {data.get('region')}, {data.get('country')}")
                print(f"🌐 ISP: {data.get('org')}")
                print(f"🗺️ Coordinates: {data.get('loc')}")
        elif choice == "3":
            print("[*] Starting server in background (Ctrl+C to stop)...")
            threading.Thread(target=start_server, daemon=True).start()
        elif choice == "4":
            try:
                with open(LOG_FILE, "r") as f:
                    print("\n--- Logged Locations ---")
                    print(f.read())
            except FileNotFoundError:
                print("No log file found yet.")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

# ===== ENTRY POINT =====
if __name__ == "__main__":
    menu()
