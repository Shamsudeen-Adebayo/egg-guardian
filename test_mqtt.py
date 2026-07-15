import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("egg/+/telemetry")

def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to broker.emqx.io...")
client.connect("broker.emqx.io", 1883, 60)
client.loop_start()
time.sleep(5)
client.loop_stop()
