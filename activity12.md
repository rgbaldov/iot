# Activity 12: Remote ESP32 Control via HiveMQ Cloud + Node-RED 

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**

## Learning Objectives  
- Understand how to use MQTT protocol for IoT communication.
- Configure ESP32 to connect to an external MQTT broker.
- Build a simple **remote control dashboard** in Node-RED.
- Control ESP32 devices from anywhere in the world.

## Requirements  
- ESP32 board with MicroPython firmware
- Micro-USB cable
- RPi or computer with:
  - **Thonny IDE** (for MicroPython programming)
  - **Node-RED** installed
- HiveMQ Cloud (free account)
- Stable internet connection

## Wiring DHT11 to ESP32  
- DHT11 **VCC → 3.3V**  
- DHT11 **GND → GND**  
- DHT11 **Data → GPIO 15**

### 1. Setup HiveMQ Cloud
1. 1. Go to [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud-broker/).
2. Create a free account and new cluster.
3. Note down:
   - Broker URL (e.g., `broker.hivemq.com`)
   - Port: `1883`
   - Username & Password (if configured)
  
### 2. Flash ESP32 with MicroPython
1. You can use Thonny IDE in your PC or RPi.
2. Download the latest ESP32 MicroPython firmware.

### 3. [ESP32 Micropython Code](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/code12-1.py)
1. Add gauge widgets for temperature and humidity
2. Send an alert notification if temperature > 30°C

### 4. Setup Node-RED Dashboard
1. Open Node-RED editor → http://localhost:1880
2. Install node-red-dashboard from Palette Manager.
3. Drag the following nodes:
  - 2 Dashboard Buttons
  - MQTT Out
4. Configure MQTT Out:
  - Server: broker.hivemq.com
  - Port: 1883
  - Topic: esp32/remote
5. Button Setup:
  - Button 1 → Payload: "ON"
  - Button 2 → Payload: "OFF"
6. Connect buttons → MQTT Out → Deploy.

## Test Procedure
1. Open Node-RED Dashboard → http://localhost:1880/ui
2. Click LED ON → ESP32 LED turns ON.
3. Click LED OFF → ESP32 LED turns OFF.
4. Verify that commands work outside local WiFi (using mobile data or another network).

## Expected Outcome
1. The ESP32 connects to the internet via WiFi.
2. Node-RED dashboard sends MQTT commands through HiveMQ Cloud.
3. ESP32 responds to commands in real-time, enabling remote IoT control.
