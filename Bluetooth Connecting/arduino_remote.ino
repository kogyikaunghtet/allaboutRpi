
#include <SoftwareSerial.h>
SoftwareSerial bt (9,10);
int Fbutton, Bbutton, Lbutton, Rbutton;
void setup() {
  bt.begin (9600);
  pinMode (2, INPUT_PULLUP);
  pinMode (3, INPUT_PULLUP);
  pinMode (4, INPUT_PULLUP);
  pinMode (5, INPUT_PULLUP);
}
void loop() {
  Fbutton = digitalRead (2);
  Bbutton = digitalRead (3);
  Lbutton = digitalRead (4);
  Rbutton = digitalRead (5);
  if (Fbutton == 1 && Bbutton == 1 && Lbutton == 1 && Rbutton == 1){
    bt.println ('S');
    delay (100);
  }
  else if (Fbutton == 0){
    bt.println ('F');
    delay (100);
  }
  else if (Bbutton == 0){
    bt.println ('B');
    delay (100);
  }
  else if (Lbutton == 0){
    bt.println ('L');
    delay (100);
  }
  else if (Rbutton == 0){
    bt.println ('R');
    delay (100);
  }
}

