# MQTT

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## 1. Introduction to MQTT
- **MQTT (Message Queuing Telemetry Transport)** is a lightweight publish/subscribe messaging protocol.
- Designed for:
  - Low-bandwidth
  - High-latency
  - Unreliable networks
- Widely used in **IoT (Internet of Things)** for device communication.

## 2. Key Concepts

### a. Broker
- Central server that receives and distributes messages.
- Popular brokers: **Mosquitto, HiveMQ, EMQX**.

### b. Client
- Devices or applications that connect to the broker.
- Can be:
  - **Publisher**: sends messages
  - **Subscriber**: receives messages

### c. Topic
- Hierarchical string used to categorize messages.
- Example:  
  - `home/livingroom/temperature`
  - `sensors/esp32/humidity`

### d. Message
- Data payload sent between publisher and subscriber.
- Typically JSON, text, or binary.

### e. QoS (Quality of Service)
- **QoS 0**: At most once (fire and forget)
- **QoS 1**: At least once (acknowledged delivery)
- **QoS 2**: Exactly once (safest, but slowest)

## 3. MQTT Workflow
1. A **client (publisher)** connects to the broker.
2. Publisher sends a message to a **topic**.
3. Broker receives the message.
4. All **subscribers** to that topic get the message.


## 4. Example Use Cases
- **Home Automation**: IoT devices reporting temperature, humidity, lights status.
- **Industry 4.0**: Machine-to-machine communication.
- **Healthcare**: Wearables sending patient vitals.
- **Agriculture**: Sensors monitoring soil moisture.

## 5. Hands-On Example

### Install Mosquitto Broker
```bash
# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
