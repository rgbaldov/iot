# Activity 6: ESP32 Web-based Temperature & Humidity Monitor

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## Objective:  
To interface an **ESP32** with a **DHT11 sensor** and create a **web server** to display real-time temperature and humidity readings. The ESP32 hosts a simple web page accessible from any device connected to the same WiFi network.  

## Objectives:  
- Connect and configure the DHT11 sensor with ESP32.  
- Set up the ESP32 as a web server.  
- Display temperature and humidity data on a webpage that refreshes automatically.  

## Materials:  
- ESP32 development board  
- DHT11 sensor  
- Breadboard & jumper wires  
- Arduino IDE  

## Wiring (ESP32 + DHT11):  
- DHT11 VCC → **3.3V (ESP32)**  
- DHT11 GND → **GND (ESP32)**  
- DHT11 DATA → **GPIO 4 (ESP32)**  

## Arduino Code:
Install the following libraries in Arduino IDE:  
- **DHT sensor library by Adafruit**  
- **Adafruit Unified Sensor**  

```cpp
#include <WiFi.h>
#include "DHT.h"

#define DHTPIN 4      // DHT11 data pin
#define DHTTYPE DHT11 // Sensor type
DHT dht(DHTPIN, DHTTYPE);

// Replace with your network credentials
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  dht.begin();

  // Connect to WiFi
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected!");
  Serial.print("ESP32 IP Address: ");
  Serial.println(WiFi.localIP());

  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (!client) return;

  String request = client.readStringUntil('\r');
  client.flush();

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    humidity = 0;
    temperature = 0;
  }

  // HTML page
  String html = "<!DOCTYPE html><html>";
  html += "<head><meta name='viewport' content='width=device-width, initial-scale=1.0'>";
  html += "<title>ESP32 DHT11 Monitor</title></head>";
  html += "<body style='font-family:Arial; text-align:center;'>";
  html += "<h2>ESP32 DHT11 Temperature & Humidity</h2>";
  html += "<p><b>Temperature:</b> " + String(temperature) + " °C</p>";
  html += "<p><b>Humidity:</b> " + String(humidity) + " %</p>";
  html += "<p>Page refreshes every 5s</p>";
  html += "<meta http-equiv='refresh' content='5'>";
  html += "</body></html>";

  client.println("HTTP/1.1 200 OK");
  client.println("Content-type:text/html");
  client.println();
  client.print(html);
  client.stop();
}
