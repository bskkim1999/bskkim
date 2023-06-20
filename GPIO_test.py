import RPi.GPIO as GPIO
import time

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT)
"""
pin_pwm = GPIO.PWM(pin, 500)  #(pin, frequency)


pin_pwm.start(0)    #(dutycycle)


while True:

    try:

        #pwm
        
        for i in range(0,101,1):
            print("{}".format(i))
            pin_pwm.ChangeDutyCycle(i)

            time.sleep(5)
        
        GPIO.output(pin, 1)
        time.sleep(1)
        GPIO.output(pin, 0)
        time.sleep(1)


    except:
        print("finish!!")
        GPIO.cleanup()
        pin_pwm.stop()

        exit(1)
"""

while True:
    GPIO.output(pin, 1)
   # time.sleep(0.1)

    #GPIO.output(pin, 0)
    #time.sleep(0.1)

