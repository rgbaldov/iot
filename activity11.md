# Activity 11: ESP32 MicroPython + DHT11 + Node-RED  

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**

## Learning Objectives  
- Configure ESP32 to read sensor data with MicroPython  
- Connect ESP32 to WiFi and publish data to an MQTT broker  
- Use Node-RED to subscribe, display, and plot sensor values

## Requirements  
- ESP32 board  
- USB data cable  
- DHT11 sensor + 10k resistor  
- Breadboard + jumper wires  
- RPi or computer with:  
- **Thonny IDE** (for ESP32 MicroPython programming)  
- **Node-RED** installed  
- **Mosquitto MQTT broker** running  

## Wiring DHT11 to ESP32  
- DHT11 **VCC → 3.3V**  
- DHT11 **GND → GND**  
- DHT11 **Data → GPIO 15**

### 1. [ESP32 Micropython Code](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/code11_1.py)

### 2. Node-RED Flow
1. Open Node-RED and import this [flow](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/code11_2.json)
2. Deploy the flow.
3. Open the Node-RED Dashboard (http://localhost:1880/ui).
4. Observe temperature and humidity values plotted live.

### 3.Additional Tasks
1. Add gauge widgets for temperature and humidity
2. Send an alert notification if temperature > 30°C

## Required Screenshot Outputs
1. Hardware Setup
2. Node-RED flow
2. MQTT published output
3. Dashboard
