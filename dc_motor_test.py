import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

enA=16
ln1=20
ln2=21

enB=8
ln3=7
ln4=1

power_right=26

GPIO.setup(enA, GPIO.OUT)
GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(ln3, GPIO.OUT)
GPIO.setup(ln4, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)
GPIO.setup(power_right, GPIO.OUT)

enA_pwm=GPIO.PWM(enA, 100) 
enB_pwm=GPIO.PWM(enB, 100)

enA_pwm.start(0)
enB_pwm.start(0)

while True:
    try:
        enA_pwm.ChangeDutyCycle(100)
        enB_pwm.ChangeDutyCycle(100)
        GPIO.output(power_right, 1)
        
        GPIO.output(ln1, 0)
        GPIO.output(ln2, 1)

        GPIO.output(ln3, 1)
        GPIO.output(ln4, 0)

    except:
        print("interrupt!!!!!!!!!")
        GPIO.cleanup()
        #enA_pwm.stop()
        enB_pwm.stop()
        exit(1)
