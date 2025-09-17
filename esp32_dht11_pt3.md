# Activity 7: ESP32 + DHT22 Sensor Simulation (Wokwi)

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## Objective:  
To use an **ESP32** with a **DHT22** in the [Wokwi Simulator](https://wokwi.com/) to read **temperature** and **humidity** data from the sensor and display it on the **serial monitor**  

## Materials:  
- ESP32  
- DHT22 sensor  
- Jumper wires  
- Wokwi Online Simulator  

## Wiring (ESP32 + DHT22):  
- DHT22 VCC → **3.3V (ESP32)**  
- DHT22 GND → **GND (ESP32)**  
- DHT22 DATA → **GPIO 4 (ESP32)**  

## Steps:
1. Go to [Wokwi](https://wokwi.com) → **Start New Project** → select **ESP32**.  
2. Add a **DHT22 sensor** from the parts library.  
3. Connect the pins as shown in the wiring diagram.  
4. Open the **Library Manager** → search and install:  
   - DHT sensor library by Adafruit  
   - Adafruit Unified Sensor  
5. Copy and paste the code below into the Arduino editor.  
6. Click **Start Simulation** ▶️.  
7. Open the **Serial Monitor** to see temperature and humidity readings

## [Arduino Code](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/activity5.ino):
