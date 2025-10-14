# Activity 15: IoT Data Logging Using ESP32, DHT11, MQTT, ThingSpeak, and Local Database

## Objective
To measure temperature and humidity using a DHT11 sensor connected to an ESP32, publish the data via MQTT to **ThingSpeak**, and also log the readings to a **local database** for offline storage

## Components Required
| Component | Description |
|------------|-------------|
| ESP32 | Microcontroller with Wi-Fi |
| DHT11 | Temperature and humidity sensor |
| Breadboard & Jumpers | For connections |
| Laptop/PC | For programming and database logging |
| Internet Connection | Required for MQTT and ThingSpeak |

## Circuit Connections
| DHT11 Pin | Connects To |
|------------|-------------|
| VCC | 3.3V on ESP32 |
| GND | GND on ESP32 |
| DATA | GPIO 4 (can be changed in code) |

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
| Parameter | Value |
|------------|--------|
| Broker | `mqtt3.thingspeak.com` |
| Port | `1883` |
| Username | ThingSpeak username |
| Password | MQTT API Key |
| Topic | `channels/<channelID>/publish` |

## [MicroPython Code](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/activity13.py) (ESP32 + DHT11 + ThingSpeak + Local DB)
> **Note:** ESP32 doesn’t have native SQLite support, but we can simulate a *local database* by saving readings in a text/CSV file.  
> For PC simulation, use the **Python version** below with real SQLite.
