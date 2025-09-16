# Activity 5: ESP32 Temperature & Humidity Monitor (Serial Monitor)

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## Objective:  
To interface a **DHT11 sensor** with an **ESP32** and display real-time temperature and humidity readings on the Arduino Serial Monitor.  

## Materials: 
- ESP32 development board  
- DHT11 sensor  
- Breadboard & jumper wires  
- Arduino IDE  

## Wiring (ESP32 + DHT11):  
- DHT11 VCC → **3.3V (ESP32)**  
- DHT11 GND → **GND (ESP32)**  
- DHT11 DATA → **GPIO 4 (ESP32)**  

## [Arduino Code](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/activity5.ino):
Install libraries:  
- **DHT sensor library by Adafruit**  
- **Adafruit Unified Sensor**
