# Manila Weather Dashboard: Node-RED Guide

**Prepared by:**  
[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**

This guide details how to build a real-time dashboard for **Manila Temperature (°C)** and **Relative Humidity** using Node-RED and the OpenWeatherMap API.

## 🛠️ Step 1: Install Required Nodes
1. Open Node-RED.
2. Go to **Menu (≡) > Manage palette > Install**.
3. Search for and install:
   * `node-red-dashboard`
   * `node-red-node-openweathermap`

## 🔑 Step 2: Get your API Key
1. Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/api).
2. Generate an **API Key**.
   > **Note:** New keys usually take **2 hours** to activate. If you get a "401 Unauthorized" error, just wait a bit longer!

## 🏗️ Step 3: Setup the Flow Logic

### 1. The Trigger
* Drag an **Inject** node. 
* Set **Repeat** to `interval` (every 15 minutes is safe for free tiers).

### 2. The Weather Query
* Drag an **OpenWeatherMap** node.
* **API Key:** Paste your key here.
* **City:** `Manila`
* **Country:** `PH`

### 3. The Logic (Change Nodes)
* **Temp Node:** Create a **Change** node. Set `msg.payload` to `msg.payload.tempc`.
* **Humidity Node:** Create a **Change** node. Set `msg.payload` to `msg.payload.humidity`.

## 📊 Step 4: The Dashboard UI
1. **Temperature Gauge:**
   * Type: `Gage`
   * Label: `Manila Temperature`
   * Units: `°C`
   * Range: `20` to `45`
2. **Humidity Gauge:**
   * Type: `Gage`
   * Label: `Manila Humidity`
   * Units: `%`
   * Range: `0` to `100`
