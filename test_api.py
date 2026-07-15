import urllib.request
import json
import uuid

base_url = "https://egg-guardian-api.onrender.com/api/v1"
email = f"test_{uuid.uuid4().hex[:8]}@example.com"
password = "Password123!"

# Register
print(f"Registering {email}...")
data = json.dumps({
    "email": email,
    "password": password,
    "full_name": "Test User",
    "job_role": "Tester"
}).encode("utf-8")
req = urllib.request.Request(f"{base_url}/auth/register", data=data, headers={"Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req) as response:
        print("Registered.")
except Exception as e:
    print(f"Register failed: {e}")
    if hasattr(e, 'read'):
        print(e.read().decode())
    exit(1)

# Login
print("Logging in...")
data = json.dumps({
    "email": email,
    "password": password
}).encode("utf-8")
req = urllib.request.Request(f"{base_url}/auth/login", data=data, headers={"Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req) as response:
        token = json.loads(response.read().decode())["access_token"]
        print("Logged in.")
except Exception as e:
    print(f"Login failed: {e}")
    if hasattr(e, 'read'):
        print(e.read().decode())
    exit(1)

# Get alerts
print("Getting alerts...")
req = urllib.request.Request(f"{base_url}/alerts", headers={"Authorization": f"Bearer {token}"})
try:
    with urllib.request.urlopen(req) as response:
        alerts = json.loads(response.read().decode())
        print(f"Total alerts: {len(alerts)}")
        if alerts:
            print(f"Sample alert: {alerts[0]}")
except Exception as e:
    print(f"Alerts failed: {e}")

# Get devices
print("Getting devices...")
req = urllib.request.Request(f"{base_url}/devices", headers={"Authorization": f"Bearer {token}"})
try:
    with urllib.request.urlopen(req) as response:
        devices = json.loads(response.read().decode())
        print(f"\nTotal devices: {len(devices)}")
        for d in devices:
            print(f"Device: {d['device_id']}")
            
            # Get telemetry for device
            try:
                treq = urllib.request.Request(f"{base_url}/devices/{d['id']}/telemetry?hours=24", headers={"Authorization": f"Bearer {token}"})
                with urllib.request.urlopen(treq) as tresp:
                    tel = json.loads(tresp.read().decode())
                    print(f"  Telemetry count: {tel['count']}")
            except Exception as e:
                print(f"  Failed to get telemetry: {e}")
except Exception as e:
    print(f"Devices failed: {e}")
