import RPi.GPIO as GPIO
import time

ln1=20
ln2=21


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

enA=GPIO.PWM(16, 100)
enA.start(100)


while(1):
    try:
        GPIO.output(ln1, 1)
        GPIO.output(ln2, 0)
        GPIO.PWM(16, 100)

    except:
        GPIO.cleanup()
        enA.stop()    

    