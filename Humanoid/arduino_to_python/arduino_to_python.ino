#include <String.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  String stringOne = "HELLO WORLD";
  // put your main code here, to run repeatedly:
  Serial.println(stringOne);
  delay(1000);
}
