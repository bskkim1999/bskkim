import RPi.GPIO as GPIO
import time

ln1=20
ln2=21
enA=12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)

enA_pwm=GPIO.PWM(enA, 1000)   #(pin, freq)

enA_pwm.start(0)   #(dutycycle)  0 ~ 100


while(1):
    try:
        print("a")
        
        GPIO.output(ln1, 0)
        GPIO.output(ln2, 1)
        
        enA_pwm.ChangeDutyCycle(100)  #(dutycycle)
        time.sleep(0.5)
        enA_pwm.ChangeDutyCycle(10)  #(dutycycle)
        time.sleep(0.5)

    except:
        print("interrupt")
        GPIO.cleanup()
        enA_pwm.stop()    
        exit(1)
    