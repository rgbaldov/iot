# Activity 9: Node-RED + MQTT + OpenWeatherMap (with Dashboard)

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**

## Learning Objectives
- Fetch live weather data from OpenWeatherMap API.
- Publish weather data to an MQTT broker.
- Visualize temperature, humidity, and conditions using Node-RED Dashboard (gauges + charts).
- Practice JSON parsing and MQTT message handling.

## Materials / Requirements
- Node-RED (running locally or on Raspberry Pi).
- MQTT broker (e.g., Mosquitto).
- OpenWeatherMap API key (free at https://openweathermap.org/).
- Node-RED Dashboard nodes installed (`node-red-dashboard`).
- Internet connection.

## Setup
1. Sign up at OpenWeatherMap and get your **API Key**.
2. Start your MQTT broker (default: `mqtt://localhost:1883`).
3. Open Node-RED (`http://localhost:1880`).
4. Install dashboard nodes if missing:
5. Import the provided [flow JSON](https://raw.githubusercontent.com/rgbaldov/iot/refs/heads/main/activity9.json) file (`import → clipboard → paste JSON → import`).
6. Edit the `Build OWM URL` function node: _const apiKey = "YOUR_OPENWEATHERMAP_API_KEY"; // replace with your key_
7. Configure the MQTT broker settings inside MQTT nodes.
8. Deploy the flow.
9. Dashboard preview: _http://localhost:1880/ui_

## Required Screenshot Outputs
1. Node-RED flow
2. MQTT published output
3. Dashboard


