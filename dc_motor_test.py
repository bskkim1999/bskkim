import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#<<핀 헤더 설정>>
##뒷바퀴##
#오른쪽 뒷바퀴
enA_back=16
ln1_back=20
ln2_back=21
#왼쪽 뒷바퀴
enB_back=8
ln3_back=7
ln4_back=1

power_right=26

##앞바퀴##
#오른쪽 앞바퀴






GPIO.setup(enA_back, GPIO.OUT)
GPIO.setup(ln1_back, GPIO.OUT)
GPIO.setup(ln2_back, GPIO.OUT)
GPIO.setup(ln3_back, GPIO.OUT)
GPIO.setup(ln4_back, GPIO.OUT)
GPIO.setup(enB_back, GPIO.OUT)
GPIO.setup(power_right, GPIO.OUT)

enA_pwm_back=GPIO.PWM(enA_back, 100) 
enB_pwm_back=GPIO.PWM(enB_back, 100)

enA_pwm_back.start(0)
enB_pwm_back.start(0)

while True:
    try:
        enA_pwm_back.ChangeDutyCycle(100)
        enB_pwm_back.ChangeDutyCycle(100)
        GPIO.output(power_right, 1)
        
        GPIO.output(ln1_back, 0)
        GPIO.output(ln2_back, 1)

        GPIO.output(ln3_back, 1)
        GPIO.output(ln4_back, 0)

    except:
        print("interrupt!!!!!!!!!")
        GPIO.cleanup()
        enA_pwm_back.stop()
        enB_pwm_back.stop()
        exit(1)
