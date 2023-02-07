#include <stdio.h>
#include <wiringPi.h>


int LED_board = 11;
int main(){

    wiringPiSetupGpio();
   pinMode(LED_board, OUTPUT);


    while(1){

            digitalWrite(LED_board, HIGH); 
            delay(500);                       
            digitalWrite(LED_board, LOW); 
            delay(500);  
    }
                      

    return 0;
}