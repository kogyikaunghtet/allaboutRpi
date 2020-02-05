char c;
void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    c = Serial.read();
    Serial.println (c);
  }
}
