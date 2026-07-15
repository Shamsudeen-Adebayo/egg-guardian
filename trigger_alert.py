import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime, timezone

def publish_alert(broker):
    client = mqtt.Client()
    try:
        client.connect(broker, 1883, 60)
        client.loop_start()
        
        topic = "egg/eggpod-01/telemetry"
        payload = {
            "device_id": "eggpod-01",
            "ts": datetime.now(timezone.utc).isoformat(),
            "temp_c": 45.0, # Definitely triggers the high alert!
        }
        
        print(f"Publishing 45.0°C to {broker}...")
        client.publish(topic, json.dumps(payload), qos=1)
        time.sleep(2)
        client.loop_stop()
        print(f"Successfully sent to {broker}!")
    except Exception as e:
        print(f"Failed to connect to {broker}: {e}")

publish_alert("broker.hivemq.com")
publish_alert("broker.emqx.io")
