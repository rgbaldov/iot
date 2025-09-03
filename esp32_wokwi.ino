#define LED_PIN 5

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH); // turn LED on
  delay(1000);                 // wait 1 second
  digitalWrite(LED_PIN, LOW);  // turn LED off
  delay(1000);                 // wait 1 second
}
