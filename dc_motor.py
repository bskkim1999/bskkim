import RPi.GPIO as GPIO
import time

ln1=20
ln2=21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)

while(1):
    GPIO.output(ln1, 1)
    
    GPIO.output(ln2, 0)
    