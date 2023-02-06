import RPi.GPIO as GPIO


ledpin1 =21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ledpin1, GPIO.OUT)

#pwm = GPIO.PWM(led_pin, 10.0)
GPIO.output(ledpin1,1)

#pwm.start(50.0)


#try:
    #while True:
        #pass

#except KeyboardInterrupt:
    #pass

#pwm.stop()
#GPIO.cleanup()
