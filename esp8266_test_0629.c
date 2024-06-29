#include <Arduino.h>


// SG90 서보모터를 제어하는 핀 번호
const int servoPin = 5;
// 각도에 따른 펄스 길이 계산 함수
int calculatePulseWidth(int angle) {
  // 서보모터의 펄스 길이는 1ms (0도)에서 2ms (180도) 사이
  // 1ms = 1000us, 2ms = 2000us
  int pulseWidth = map(angle, 0, 180, 300, 2500);
  return pulseWidth;
}

// 펄스 신호를 생성하는 함수
void writeServo(int pin, int angle) {
  int pulseWidth = calculatePulseWidth(angle);
  // 50Hz 주기 = 20ms 주기 (서보모터의 주기)
  // 20ms = 20000us
  //int pulseWidth = 700;
  //int pulseWidth = 1400;
  digitalWrite(pin, HIGH);
  delayMicroseconds(pulseWidth);
  digitalWrite(pin, LOW);
  delayMicroseconds(20000 - pulseWidth);
}

void turn_on(void) {
  
  for(int i=0 ; i<100 ; i++){
    writeServo(servoPin, 45);   //45 degree
    delay(1);
  }
  

  for(int i=0 ; i<100 ; i++){
    writeServo(servoPin, 180);  //180 degree
    delay(1);
  }
    
}



void setup() {
  // 서보모터 핀을 출력으로 설정
  pinMode(servoPin, OUTPUT);
  Serial.begin(9600);  
}

void loop() {

}
