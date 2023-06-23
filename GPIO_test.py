import RPi.GPIO as GPIO
import time

pin = 21
#pin2 =  3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT)
#GPIO.setup(pin2, GPIO.OUT)

#pin_pwm = GPIO.PWM(pin, 100)  #(pin, frequency)
#pin_pwm2 = GPIO.PWM(pin2, 100)  #(pin, frequency)

#pin_pwm.start(0)    #(dutycycle)
#pin_pwm2.start(0)    #(dutycycle)

i=0
i2=0
start_time = 0

while True:

    try:

        #GPIO.output(pin, 0)
        #time.sleep(0.0001)
        GPIO.output(pin, 1)
        #time.sleep(0.0001)

    except:
        print("interrupt!!!!!!!!!")
        GPIO.cleanup()
        GPIO.output(pin, 0)
        exit(1)




