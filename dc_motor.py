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
enA.start(70)


while(1):
    try:
        GPIO.output(ln1, 0)
        GPIO.output(ln2, 1)
        GPIO.PWM(16, 70)

    except:
        GPIO.cleanup()
        enA.stop()    

    