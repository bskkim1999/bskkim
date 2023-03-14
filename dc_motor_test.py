import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

enA=16
ln1=20
ln2=21
power=26

GPIO.setup(enA, GPIO.OUT)
GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(power, GPIO.OUT)

enA_pwm=GPIO.PWM(enA, 100) 

enA_pwm.start(0)

while True:
    enA_pwm.ChangeDutyCycle(100)
    GPIO.output(power, 1)
    GPIO.output(ln1, 0)
    GPIO.output(ln2, 1)