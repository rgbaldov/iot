import network
import time
from umqtt.simple import MQTTClient
from machine import Pin

# WiFi credentials
SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASS"

# HiveMQ Cloud MQTT broker credentials
MQTT_BROKER = "YOUR_CLUSTER.s1.eu.hivemq.cloud"
MQTT_PORT = 8883  # Use 1883 if broker allows non-SSL
MQTT_USER = "your-username"
MQTT_PASS = "your-password"
TOPIC = "esp32/remote"

# Connect WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)
print("Connecting to WiFi", end="")
while not wifi.isconnected():
    print(".", end="")
    time.sleep(1)
print("\nConnected:", wifi.ifconfig())

# Setup LED
led = Pin(2, Pin.OUT)

# MQTT callback
def sub_cb(topic, msg):
    print("Received:", msg)
    if msg == b"ON":
        led.value(1)
    elif msg == b"OFF":
        led.value(0)

# MQTT setup
client = MQTTClient("esp32client", MQTT_BROKER, port=MQTT_PORT,
                    user=MQTT_USER, password=MQTT_PASS, ssl=False)
client.set_callback(sub_cb)
client.connect()
client.subscribe(TOPIC)
print("Subscribed to", TOPIC)

# Listen loop
while True:
    client.wait_msg()
