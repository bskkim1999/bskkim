import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


for ii in range(1,26):
    GPIO.setup(ii, GPIO.OUT)



while True:
    for i in range(1, 26):
        GPIO.output(i, 1)


