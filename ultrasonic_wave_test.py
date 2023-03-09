import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 19
ECHO = 26

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, 0)
print("초음파 출력 초기화")
time.sleep(0.5)

start=0
stop=0

try:
    while True:
       
        GPIO.output(TRIG,1)
        time.sleep(0.00001)        # 10uS의 펄스 발생을 위한 딜레이
        
        GPIO.output(TRIG, 0)
        
        if GPIO.input(ECHO)==0:
            start = time.time()     # Echo핀 상승 시간값 저장
            print("a")
            
            
        elif GPIO.input(ECHO)!=0:
            stop = time.time()      # Echo핀 하강 시간값 저장
            print("b")
            
            
        check_time = stop - start
        distance = check_time * 34300 / 2

        print("{}".format(check_time))
        print("Distance : %.1f cm" % distance)
        time.sleep(5)
        
except KeyboardInterrupt:
    print("거리 측정 완료 ")
    GPIO.cleanup()