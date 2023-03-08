import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


for ii in range(0,28):
    GPIO.setup(ii, GPIO.OUT)



while True:
    for i in range(0, 28):
        GPIO.output(i, 1)


