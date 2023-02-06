import RPI.GPIO as GPIO

led_pin =18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 10.0)

pwm.start(50.0)

