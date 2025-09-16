# Activity 6: ESP32 Temperature & Humidity Monitor (Serial Monitor)

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## Objective:  
To interface a **DHT11 sensor** with an **ESP32** and display real-time temperature and humidity readings on the Arduino Serial Monitor.  

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
Install libraries:  
- **DHT sensor library by Adafruit**  
- **Adafruit Unified Sensor**  

```cpp
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
