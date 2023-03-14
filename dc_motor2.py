import RPi.GPIO as GPIO
import time


#==============================헤더핀 설정========================================
#차체 왼쪽의 모터드라이브=뒷바퀴, 오른쪽 모터드라이브=앞바퀴
#왼쪽(뒷바퀴)
power_left=12

ln1_left=16
ln2_left=20  
enA_left=21

ln3_left=8
ln4_left=7
enB_left=1

#오른쪽(앞바퀴)
power_right=14

ln1_right=15
ln2_right=18
enA_right=23

ln3_right=24
ln4_right=25
enB_right=19

#============================================================================

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(power_left, GPIO.OUT)
GPIO.setup(ln1_left, GPIO.OUT)
GPIO.setup(ln2_left, GPIO.OUT)
GPIO.setup(enA_left, GPIO.OUT)
GPIO.setup(ln3_left, GPIO.OUT)
GPIO.setup(ln4_left, GPIO.OUT)
GPIO.setup(enB_left, GPIO.OUT)

GPIO.setup(power_right, GPIO.OUT)
GPIO.setup(ln1_right, GPIO.OUT)
GPIO.setup(ln2_right, GPIO.OUT)
GPIO.setup(enA_right, GPIO.OUT)
GPIO.setup(ln3_right, GPIO.OUT)
GPIO.setup(ln4_right, GPIO.OUT)
GPIO.setup(enB_right, GPIO.OUT)

#pwm핀 총 4개
enA_left_pwm=GPIO.PWM(enA_left, 100)   #(pin, freq)
enB_left_pwm=GPIO.PWM(enB_left, 100)   #(pin, freq)
enA_right_pwm=GPIO.PWM(enA_right, 100)   #(pin, freq)
enB_right_pwm=GPIO.PWM(enB_right, 100)   #(pin, freq)

enA_left_pwm.start(0)   #(dutycycle)  0 ~ 100
enB_left_pwm.start(0)   #(dutycycle)  0 ~ 100
enA_right_pwm.start(0)   #(dutycycle)  0 ~ 100
enB_right_pwm.start(0)   #(dutycycle)  0 ~ 100


#========main task================================================================

while True:
    
    enA_left_pwm.ChangeDutyCycle(100)
    enB_left_pwm.ChangeDutyCycle(100)
    enA_right_pwm.ChangeDutyCycle(100)
    enA_right_pwm.ChangeDutyCycle(100)
    
    GPIO.output(power_left, 1)
    GPIO.output(power_right, 1)

    GPIO.output(ln1_right, 0)
    GPIO.output(ln2_right, 1)
    #GPIO.output(ln3_right, 1)
    #GPIO.output(ln4_right, 0)