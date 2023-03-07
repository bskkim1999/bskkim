import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(ledpin1, GPIO.OUT)


for i in range(1, 25):
    GPIO.output(i, 1)


