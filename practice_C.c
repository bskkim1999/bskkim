#include <stdio.h>
#include <wiringPi.h>


int LED_BUILTIN = 
int main(){

    wiringPiSetupGpio();
   pinMode(LED_BUILTIN, OUTPUT);


    while(1){

            digitalWrite(LED_BUILTIN, HIGH); 
            delay(500);                       
            digitalWrite(LED_BUILTIN, LOW); 
            delay(500);  
    }
                      

    return 0;
}