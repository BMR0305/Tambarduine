#include <Servo.h>
Servo myservo;
int pos = 90;
void setup() {
  pinMode(8, OUTPUT);
  myservo.attach(9);

}

void loop() {
  /**digitalWrite(8, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(2000);                      // wait for half a second
  digitalWrite(8, LOW);   // turn the LED off by making the voltage LOW
  delay(200);**/ 
  /**for (pos =90; pos <= 135; pos+=1){
    myservo.write(pos);
    delay(10);
  }**/
  /**
  for (pos =0; pos<= 45; pos+=1){
    myservo.write(pos);
    delay(10);
  }
  
  for (pos =45; pos >= 0; pos-=1){
    myservo.write(pos);
    delay(10);
  }
 **/
   myservo.write(90);
  delay(450);
  digitalWrite(8, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(50);
  digitalWrite(8, LOW);   // turn the LED off by making the voltage LOW
  myservo.write(135);
  delay(450);
  digitalWrite(8, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(50);
  digitalWrite(8, LOW);   // turn the LED off by making the voltage LOW
  myservo.write(90);
  delay(450);
  digitalWrite(8, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(50);
  digitalWrite(8, LOW);   // turn the LED off by making the voltage LOW
  myservo.write(45);
  delay(450);
  digitalWrite(8, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(50);
  digitalWrite(8, LOW);   // turn the LED off by making the voltage LOW
  myservo.write(90);
}
