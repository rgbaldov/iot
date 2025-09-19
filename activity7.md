# Activity 7: Node-RED with MQTT Activity

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## Learning Objectives
By the end of this activity, you should be able to:
- Understand the **publish/subscribe** workflow in MQTT.
- Configure **Node-RED** with MQTT broker connections.
- Create a simple **flow** to publish and subscribe to a topic.
- Visualize message exchange using the **debug panel**.

## Requirements
- Node-RED installed (`npm install -g node-red`)
- MQTT Broker (e.g., **Mosquitto**) running locally or remotely
- Basic familiarity with Node-RED nodes

## Instructions

### 1. Start MQTT Broker
If using **Mosquitto** locally (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto

### 2. [Node-Red](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/mqtt.json)
