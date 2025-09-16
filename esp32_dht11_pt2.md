# Activity 6: ESP32 Web-based Temperature & Humidity Monitor

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## Objective:  
To interface an **ESP32** with a **DHT11 sensor** and create a **web server** to display real-time temperature and humidity readings. The ESP32 hosts a simple web page accessible from any device connected to the same WiFi network.  

## Objectives:  
- Connect and configure the DHT11 sensor with ESP32.  
- Set up the ESP32 as a web server.  
- Display temperature and humidity data on a webpage that refreshes automatically.  

## Materials:  
- ESP32 development board  
- DHT11 sensor  
- Breadboard & jumper wires  
- Arduino IDE  

## Wiring (ESP32 + DHT11):  
- DHT11 VCC → **3.3V (ESP32)**  
- DHT11 GND → **GND (ESP32)**  
- DHT11 DATA → **GPIO 4 (ESP32)**  

## [Arduino Code](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/activity6.ino):
Install the following libraries in Arduino IDE:  
- **DHT sensor library by Adafruit**  
- **Adafruit Unified Sensor**
