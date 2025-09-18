# IoT Weather Monitoring with Node-RED, Raspberry Pi, DHT11, and OpenWeatherMap

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## Learning Objectives:
- Interface a **DHT11 temperature & humidity sensor** with RPi.
- Set up **Node-RED flows** to acquire sensor readings.  
- Retrieve **real-time weather data** from the OpenWeatherMap API.  
- Compare **local sensor data vs. online weather service data** on a Node-RED Dashboard.  
- Send alerts when thresholds are exceeded.  

## Materials Needed
- RPi  
- DHT11 sensor + 10kΩ resistor  
- Jumper wires & breadboard  
- Node-RED installed on RPi  
- OpenWeatherMap API key (use your same account last MFELEC1)

## Wiring (DHT11 → Raspberry Pi GPIO)
- **DHT11 VCC → 3.3V (Pin 1)**  
- **DHT11 GND → GND (Pin 6)**  
- **DHT11 DATA → GPIO4 (Pin 7)**  
- Pull-up resistor (10kΩ) between VCC and DATA  

## [Node-RED Flow Setup](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/dht11.json)

### 1. DHT11 Sensor Input
- Install Node-RED DHT sensor node:  
 
