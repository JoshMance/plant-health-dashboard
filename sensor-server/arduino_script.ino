/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-soil-moisture-sensor
 */

#define AOUT_PIN A0 // Arduino pin that connects to AOUT pin of moisture sensor

void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(AOUT_PIN); // read the analog value from sensor

  Serial.println(value);

  delay(500);
}