#include <Servo.h>
Servo myservo;
int pos = 0;
void setup() {
  //pinMode(8, OUTPUT);
  myservo.attach(9);

}

void loop() {
  /**digitalWrite(8, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(2000);                      // wait for half a second
  digitalWrite(8, LOW);   // turn the LED off by making the voltage LOW
  delay(200);**/ 
  /**for (pos =0; pos <= 180; pos+=1){
    myservo.write(pos);
    delay(15);
  }
  for (pos =180; pos>= 0; pos-=1){
    myservo.write(pos);
    delay(15);
  }
  myservo.detach();**/
  /**
  for (pos =45; pos >= 0; pos-=1){
    myservo.write(pos);
    delay(10);
  }**/
  myservo.write(90);
  delay(250);
  myservo.write(135);
  delay(250);
  myservo.write(90);
  delay(250);
  myservo.write(45);
  delay(250);
  myservo.write(90);
  delay(250);
  while (1){
    
  }
  
}
