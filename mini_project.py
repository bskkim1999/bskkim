import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


for ii in range(1,25):
    GPIO.setup(ii, GPIO.OUT)


for i in range(1, 25):
    GPIO.output(i, 1)


