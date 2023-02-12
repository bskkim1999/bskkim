#include <wiringPi.h>
#include "servo.h"

 
int servoPin = 21;

Servo servo; 

int angle = 0; // servo position in degrees 

int main(){

    wiringPiSetupGpio();    //USE BCM
    servo.attach(servoPin); 

    // scan from 0 to 180 degrees
  for(angle = 0; angle < 180; angle++) 
  { 
    servo.write(angle); 
    delay(20); 
  } 
  // now scan back from 180 to 0 degrees
  for(angle = 180; angle > 0; angle--) 
  { 
    servo.write(angle); 
    delay(20); 
  } 

}



  
  


