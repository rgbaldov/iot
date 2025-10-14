# Activity 13: IoT Data Logging Using ESP32, DHT11, MQTT, ThingSpeak, and Local Database

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**

## Objective
To measure temperature and humidity using a DHT11 sensor connected to an ESP32, publish the data via MQTT to **ThingSpeak**, and also log the readings to a **local database** for offline storage

## Components Required
- ESP32
- DHT11
- Breadboard & Jumpers
- Laptop/PC or RPi
- Internet connection (required for MQTT and ThingSpeak)

## Circuit Connections
- DHT11 **VCC → 3.3V**  
- DHT11 **GND → GND**  
- DHT11 **Data → GPIO 15**

## ThingSpeak Setup
1. Go to [ThingSpeak](https://thingspeak.com/) and log in.  
2. Create a **New Channel**:
   - Field 1: Temperature  
   - Field 2: Humidity  
3. Click **Save Channel**.
4. Go to your **MQTT API Keys** and note:
   - **Username**
   - **MQTT API Key**
   - **Channel ID**

## MQTT Broker Info for ThingSpeak
- Broker: _mqtt3.thingspeak.com_
- Port: _1883_
- Username: _ThingSpeak username_
- Password: _MQTT API Key_
- Topic: _channels/<channelID>/publish_

## [MicroPython Code](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/activity13.py) (ESP32 + DHT11 + ThingSpeak + Local DB)
> **Note:** ESP32 doesn’t have native SQLite support, but we can simulate a *local database* by saving readings in a text/CSV file. 
