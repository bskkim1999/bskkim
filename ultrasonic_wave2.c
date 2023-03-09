#include <stdio.h>                              // stdio.h 파일 포함( printf() 사용하기 위해 )
#include <wiringPi.h>                           // wiringPi.h 파일 포함

int main(void )
{
   Float distance, start, stop;

    int echo = 20;
    int trig =21;

   wiringPiSetupGpio();
                                                // wiringPi 기준으로 PIN 번호 매김
   pinMode(trig, OUTPUT);                          // wiringPi GPIO 0번  = Python(BCM) 17번 
   pinMode(echo, INPUT);                           // wiringPi GPIO 1번  = Python(BCM) 18번

  while(1){
  
      digitalWrite(trig,0);                        // wiringPi 0번핀을 Low로 출력
      digitalWrite(trig,1);                        // wiringPi 0번핀을 High로 출력
      delayMicroseconds(10);                    // 10마이크로초 동안 멈춘다
      digitalWrite(trig,0);
    
      while(digitalRead(echo) == 0)                // wiringPi 1번핀을 Low일 경우
         start = micros();                      // 마이크로초 저장
      while(digitalRead(echo) == 1)                // wiringPi 1번핀을 High일 경우
         stop = micros();                       // 마이크로초 저장

      distance = (stop – start) / 58;           // 시간의 차이를 이용하여 거리를 도출한다
      printf("%f", distance);  
      delay(1000);
  }

  return 0;
}