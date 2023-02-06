import RPi.GPIO as GPIO
import time

led_pin =21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(led_pin, GPIO.OUT)

#pwm = GPIO.PWM(led_pin, 10.0)
GPIO.output(led_pin,1)

#pwm.start(50.0)


#try:
    #while True:
        #pass

#except KeyboardInterrupt:
    #pass

#pwm.stop()
#GPIO.cleanup()
