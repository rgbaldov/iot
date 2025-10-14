import network
import time
from umqtt.simple import MQTTClient
from machine import Pin
import dht

# ---- USER SETTINGS ----
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
THINGSPEAK_BROKER = "mqtt3.thingspeak.com"
CHANNEL_ID = "YOUR_CHANNEL_ID"
MQTT_USERNAME = "YOUR_MQTT_USERNAME"
MQTT_API_KEY = "YOUR_MQTT_API_KEY"
TOPIC = f"channels/{CHANNEL_ID}/publish"

# ---- WIFI SETUP ----
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)
    print("Connected:", wlan.ifconfig())

# ---- SENSOR SETUP ----
sensor = dht.DHT11(Pin(4))

# ---- LOCAL FILE LOGGING ----
def log_to_local(temp, hum):
    try:
        with open("datalog.csv", "a") as f:
            t = time.localtime()
            timestamp = f"{t[0]}-{t[1]}-{t[2]} {t[3]}:{t[4]}:{t[5]}"
            f.write(f"{timestamp},{temp},{hum}\n")
        print("Logged locally:", timestamp, temp, hum)
    except Exception as e:
        print("Log error:", e)

# ---- MQTT PUBLISH ----
def publish_mqtt(client, temp, hum):
    payload = f"field1={temp}&field2={hum}"
    client.publish(TOPIC, payload)
    print(f"Published -> Temp: {temp}°C | Humidity: {hum}%")

# ---- MAIN LOOP ----
def main():
    connect_wifi()
    client = MQTTClient("ESP32_Client", THINGSPEAK_BROKER, user=MQTT_USERNAME, password=MQTT_API_KEY)
    client.connect()
    print("Connected to ThingSpeak MQTT Broker.")
    
    while True:
        try:
            sensor.measure()
            temp = sensor.temperature()
            hum = sensor.humidity()
            publish_mqtt(client, temp, hum)
            log_to_local(temp, hum)
            time.sleep(20)
        except Exception as e:
            print("Error:", e)
            time.sleep(5)

main()
