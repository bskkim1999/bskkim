import RPi.GPIO as GPIO
import time

#모든 핀 헤더에 pwm이 사용 가능한 것 같다... 확실하진 않음.
pin1=16
pin2=12 #pwm
pin3=13 #pwm
pin4=18 #pwm
pin5=19 #pwm
pin6=14 #pwm

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
GPIO.setup(pin5, GPIO.OUT)
GPIO.setup(pin6, GPIO.OUT)

pin2_pwm=GPIO.PWM(pin2, 1000)  #(pin, frequency)
pin3_pwm=GPIO.PWM(pin3, 500)  #(pin, frequency)
pin4_pwm=GPIO.PWM(pin4, 100)  #(pin, frequency)
pin5_pwm=GPIO.PWM(pin5, 50)  #(pin, frequency)
pin6_pwm=GPIO.PWM(pin6, 10)  #(pin, frequency)

pin2_pwm.start(0)    #(dutycycle)
pin3_pwm.start(0)    #(dutycycle)
pin4_pwm.start(0)    #(dutycycle)
pin5_pwm.start(0)    #(dutycycle)
pin6_pwm.start(10)    #(dutycycle)

while True:
    
    try:
        #digital
        GPIO.output(pin1, 1)

        #pwm
        for i in range(0,101):
            print("{}".format(i))
            pin2_pwm.ChangeDutyCycle(i)
            pin3_pwm.ChangeDutyCycle(i)
            pin4_pwm.ChangeDutyCycle(i)
            pin5_pwm.ChangeDutyCycle(i)
            #pin6_pwm.ChangeDutyCycle(i)
            time.sleep(0.1)


    except:
        print("finish!!")
        GPIO.cleanup()
        pin2_pwm.stop()
        pin3_pwm.stop()
        exit(1)