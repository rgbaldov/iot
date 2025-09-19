# Activity 8: MQTT Messaging with Node-RED

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## Objectives:
To demonstrate how IoT devices communicate using the **MQTT protocol** through a simulated publish-subscribe setup in Node-RED

## Requirements
- Node-RED installed  
- MQTT broker (public broker like `broker.hivemq.com` or local `mosquitto`)  
- Internet connection

## Instructions
### 1. Set up MQTT Broker  
- Use a free public broker:  
  - **Broker URL:** `broker.hivemq.com`  
  - **Port:** `1883`  

### 2. Node-RED Flow Design  
**1. MQTT In Node (Subscriber):**  
- Connect to broker `broker.hivemq.com:1883`  
   - Topic: `iot/classroom/demo`  

**2. MQTT Out Node (Publisher):**  
- Same broker and topic: `iot/classroom/demo`  

**3. Inject Node:**  
- Simulates a sensor sending a message (e.g., temperature value).  

**4. Debug Node:**  
- Displays messages received by the subscriber.  

### 3. Example Messages to Publish  
- `"Temperature: 28°C"`  
- `"Humidity: 65%"`  
- `"Alert: Crack Detected!"`  

### 4. Sample [Node-RED Flow](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/mqtt.json)
