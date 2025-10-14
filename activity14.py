import requests
import time
import sqlite3
import paho.mqtt.client as mqtt

# ---- CONFIG ----
CITY = "Manila,PH"
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

THINGSPEAK_BROKER = "mqtt3.thingspeak.com"
CHANNEL_ID = "YOUR_CHANNEL_ID"
MQTT_USERNAME = "YOUR_MQTT_USERNAME"
MQTT_API_KEY = "YOUR_MQTT_API_KEY"
TOPIC = f"channels/{CHANNEL_ID}/publish"

# ---- SQLITE DATABASE ----
conn = sqlite3.connect("weather_data.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_log (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 timestamp TEXT,
 temperature REAL,
 humidity REAL
)
""")

# ---- MQTT SETUP ----
client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_API_KEY)
client.connect(THINGSPEAK_BROKER, 1883, 60)

# ---- MAIN LOOP ----
while True:
 try:
     # Fetch weather data from OpenWeatherMap
     response = requests.get(URL)
     data = response.json()
     temp = data["main"]["temp"]
     hum = data["main"]["humidity"]
     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

     # Log to local database
     cursor.execute("INSERT INTO weather_log (timestamp, temperature, humidity) VALUES (?, ?, ?)",
                    (timestamp, temp, hum))
     conn.commit()

     # Publish to ThingSpeak via MQTT
     payload = f"field1={temp}&field2={hum}"
     client.publish(TOPIC, payload)
     
     print(f"[{timestamp}] Sent -> Temp: {temp}°C | Hum: {hum}%")

     time.sleep(20)  # ThingSpeak allows updates every 15 seconds minimum

 except Exception as e:
     print("Error:", e)
     time.sleep(10)
