import RPi.GPIO as GPIO




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ledpin1, GPIO.OUT)


print("hello~~")