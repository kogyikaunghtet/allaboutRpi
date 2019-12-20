#include <SoftwareSerial.h>
SoftwareSerial bt (9,10);
int moisture;
void setup () {
  bt.begin (9600);
  Serial.begin (9600);
  pinMode (A0, INPUT);  
}
void loop () {
  moisture = analogRead (A0);
  moisture = map (moisture, 0, 1023, 100, 0);
  Serial.println (moisture);
  bt.print (moisture);
  bt.print ("\n");
  delay (1000);
}
