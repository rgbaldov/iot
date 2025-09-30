import network
import time
import dht
from machine import Pin
from umqtt.simple import MQTTClient

# MQTT Settings
MQTT_BROKER = "test.mosquitto.org"   # Or your local broker IP
MQTT_TOPIC = "esp32/dht11"

# WiFi Settings
SSID = "your_wifi_name"
PASSWORD = "your_wifi_password"

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Connecting to WiFi", end="")
while not wifi.isconnected():
    print(".", end="")
    time.sleep(1)
print("\nConnected:", wifi.ifconfig())

# Setup DHT11
sensor = dht.DHT11(Pin(15))

# Setup MQTT
client = MQTTClient("esp32_dht11", MQTT_BROKER)
client.connect()

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        msg = "Temp:{}C Hum:{}%".format(temp, hum)
        print("Publishing:", msg)
        client.publish(MQTT_TOPIC, msg)
        time.sleep(5)
    except Exception as e:
        print("Error:", e)
        time.sleep(5)
