#include <stdio.h>
#include <wiringPi.h>
#include <stdlib.h>


int main (void){


  int trig = 19 ;
  int echo = 26 ;
  int start_time, end_time ;
  float distance ;

    wiringPiSetupGpio();

 

  pinMode(trig, OUTPUT) ;
  pinMode(echo , INPUT) ;


  while(1) {

    digitalWrite(trig, LOW) ;
    delay(500) ;
    digitalWrite(trig, HIGH) ;
    delayMicroseconds(10) ;
    digitalWrite(trig, LOW) ;

    printf("a");
    while (digitalRead(echo) == 0) ;

    start_time = micros() ;

    while (digitalRead(echo) == 1) ;
    printf("b");
    end_time = micros() ;
    printf("c");
    distance = (end_time - start_time) / 29. / 2. ;

    printf("distance %.2f cm\n", distance) ;

    delay(1000);
  }

  return 0 ;

}