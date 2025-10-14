# Activity 14: ESP32 + MQTT + ThingSpeak + Local Database + OpenWeatherMap Integration

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**

## Objective
To build an IoT system that:
1. Uses **OpenWeatherMap API** to fetch real-time weather data (temperature and humidity).  
2. Publishes this data to **ThingSpeak** using **MQTT**.  
3. Logs the same data to a **local database (SQLite)** for analytics or offline storage.

This demonstrates how cloud APIs, MQTT, and IoT dashboards can be integrated into a complete IoT data pipeline.

## Components & Tools Required
- ESP32 (optional for deployment)
- Python 3 (for simulation on PC or Raspberry Pi)
- ThingSpeak account
- OpenWeatherMap API key
- SQLite (built into Python)
- Wi-Fi connection

## Step 1: ThingSpeak Setup
1. Log in to [ThingSpeak](https://thingspeak.com/).  
2. Create a **New Channel** named `Weather Station Data`.  
3. Add two fields:
   - Field 1: Temperature (°C)
   - Field 2: Humidity (%)
4. Save the channel.  
5. Go to **MQTT API Keys** and note:
   - **Username**
   - **MQTT API Key**
   - **Channel ID**

## Step 2: Get OpenWeatherMap API Key
1. Go to [https://openweathermap.org/api](https://openweathermap.org/api)
2. Sign up for a free account.
3. Copy your **API key**.
4. Find your **City ID** or use the format: api.openweathermap.org/data/2.5/weather?q=Manila,PH&appid=YOUR_API_KEY&units=metric

## Step 3: [Python Code](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/activity14.py) (with MQTT + ThingSpeak + SQLite + OpenWeatherMap)

## Step 4: Verify local DB
```bash
sqlite3 weather_data.db
sqlite> SELECT * FROM weather_log;
```

## Step 5: Verify DB on ThingSpeak
1. Go to your ThingSpeak channel view.
2. You should see:
  - Field 1 graph (Temperature)
  - Field 2 graph (Humidity)
3. The data should update every ~20 s.
