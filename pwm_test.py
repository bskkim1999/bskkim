import RPi.GPIO as GPIO
import time


pin1=16
pin2=12 #pwm
pin3=13 #pwm


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)

pin2_pwm=GPIO.PWM(pin2, 100)  #(pin, frequency)
pin3_pwm=GPIO.PWM(pin3, 100)  #(pin, frequency)

pin2_pwm.start(0)    #(dutycycle)
pin3_pwm.start(0)    #(dutycycle)

while True:
    
    try:
        #digital
        GPIO.output(pin1, 1)

        #pwm
        for i in range(0,101):
            pin2_pwm.ChangeDutyCycle(i)
            pin3_pwm.ChangeDutyCycle(i)
            time.sleep(1)


    except:
        print("finish!!")
        GPIO.cleanup()
        pin2_pwm.stop()
        pin3_pwm.stop()