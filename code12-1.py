import network
import time
from umqtt.simple import MQTTClient
from machine import Pin

# WiFi credentials
WIFI_SSID = "YOUR_WIFI"
WIFI_PASS = "YOUR_PASS"

# MQTT Broker (HiveMQ Cloud)
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_CLIENT = "esp32-client"
MQTT_TOPIC = "esp32/remote"

# Connect WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
print("✅ WiFi connected:", wifi.ifconfig())

# Connect MQTT
client = MQTTClient(MQTT_CLIENT, MQTT_BROKER, MQTT_PORT)
client.connect()
print("✅ Connected to HiveMQ Broker")

# Setup LED (built-in LED on GPIO2)
led = Pin(2, Pin.OUT)

# Callback for incoming messages
def sub_cb(topic, msg):
    print("Message:", msg)
    if msg == b"ON":
        led.value(1)
    elif msg == b"OFF":
        led.value(0)

client.set_callback(sub_cb)
client.subscribe(MQTT_TOPIC)

print("📡 Listening for remote commands...")
while True:
    client.wait_msg()
