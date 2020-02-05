#include <Wire.h>
#define SLAVE_ADDRESS 0x04
int number = 0;

void setup() {
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.println("Ready!");
}

void loop() {
}

void receiveData(int byteCount) {
  while (Wire.available()) {
    number = Wire.read();
    Serial.print("data received: ");
    Serial.println(number);
  }
}

void sendData() {
  Wire.write(number);
}
