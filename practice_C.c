#include <stdio.h>
#include <wiringPi.h>


int LED_board = 21;

int main(){
    wiringPiSetupGpio();  //BCM기준으로 핀이 바뀜
   pinMode(LED_board, OUTPUT);

   while(1){

        
        digitalWrite(LED_board, HIGH);
        delay(500);
        printf("hello\n");
        digitalWrite(LED_board, LOW);
        delay(500);
        
       
   }
                      

    return 0;
}