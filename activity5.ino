#include "DHT.h"

#define DHTPIN 4      // Pin connected to DHT11 data
#define DHTTYPE DHT11 // Define DHT type as DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  Serial.println("ESP32 DHT11 Temperature & Humidity Monitoring");
}

void loop() {
  delay(2000); // Wait a few seconds between measurements

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C  |  Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");
}
