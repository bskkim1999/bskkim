import RPi.GPIO as GPIO
import time

ledpin1 =21



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ledpin1, GPIO.OUT)



while(1):
    GPIO.output(ledpin1, 1)
    time.sleep(1)
    GPIO.output(ledpin1, 0)
    time.sleep(1)
    

