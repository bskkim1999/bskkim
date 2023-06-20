import RPi.GPIO as GPIO


pin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT)
pin_pwm = GPIO.PWM(pin, 500)  #(pin, frequency)


pin_pwm.start(0)    #(dutycycle)


while True:

    try:

        #pwm
        for i in range(0,101,1):
            print("{}".format(i))
            pin_pwm.ChangeDutyCycle(i)

            time.sleep(5)


    except:
        print("finish!!")
        GPIO.cleanup()
        pin_pwm.stop()

        exit(1)


