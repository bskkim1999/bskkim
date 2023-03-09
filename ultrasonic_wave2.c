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
    
    while (digitalRead(echo) == 0) {
        print("b")
    }

    start_time = micros() ;
    printf("%d", start_time);

    while (digitalRead(echo) == 1){
        print("c")
    }

    printf("d");
    end_time = micros() ;
    printf("%d", end_time);
    printf("e\n");
    distance = (end_time - start_time) / 29. / 2. ;

    printf("distance %.2f cm \n", distance) ;

    delay(500);
  }

  return 0 ;

}