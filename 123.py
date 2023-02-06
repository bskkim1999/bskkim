import RPi.GPIO as GPIO


ledpin =21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ledpin, GPIO.OUT)

#pwm = GPIO.PWM(led_pin, 10.0)
GPIO.output(ledpin,1)

#pwm.start(50.0)


#try:
    #while True:
        #pass

#except KeyboardInterrupt:
    #pass

#pwm.stop()
#GPIO.cleanup()
