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
