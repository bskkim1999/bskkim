import RPi.GPIO as GPIO
import time
import termios
import tty
import sys
import select
#==============================헤더핀 설정========================================
#차체 왼쪽의 모터드라이브=뒷바퀴, 오른쪽 모터드라이브=앞바퀴
#왼쪽(뒷바퀴)
power_left=12

ln1_left=16
ln2_left=20  
enA_left=21

ln3_left=8
ln4_left=7
enB_left=1

#오른쪽(앞바퀴)
power_right=14

ln1_right=15
ln2_right=18
enA_right=23

ln3_right=24
ln4_right=25
enB_right=19

#============================================================================
#기능함수들
#전진
def forward_dc():
    GPIO.output(power_left, 1)
    GPIO.output(power_right, 1)

    GPIO.output(ln1_left, 0)
    GPIO.output(ln2_left, 1)
    GPIO.output(ln3_left, 1)
    GPIO.output(ln4_left, 0)

    #GPIO.output(ln1_right, 0)
    #GPIO.output(ln2_right, 1)
    #GPIO.output(ln3_right, 1)
    #GPIO.output(ln4_right, 0)




#후진
def backward_dc():
    GPIO.output(power_left, 1)
    GPIO.output(power_right, 1)

    #GPIO.output(ln1_left, 1)
    #GPIO.output(ln2_left, 0)
    #GPIO.output(ln3_left, 0)
    #GPIO.output(ln4_left, 1)

#정지
def stop_dc():
    GPIO.output(ln1_left, 0)
    GPIO.output(ln2_left, 0)
    GPIO.output(ln3_left, 0)
    GPIO.output(ln4_left, 0)

    GPIO.output(ln1_right, 0)
    GPIO.output(ln2_right, 0)
    GPIO.output(ln3_right, 0)
    GPIO.output(ln4_right, 0)



#==============================================================================

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(power_left, GPIO.OUT)
GPIO.setup(ln1_left, GPIO.OUT)
GPIO.setup(ln2_left, GPIO.OUT)
GPIO.setup(enA_left, GPIO.OUT)
GPIO.setup(ln3_left, GPIO.OUT)
GPIO.setup(ln4_left, GPIO.OUT)
GPIO.setup(enB_left, GPIO.OUT)

GPIO.setup(power_right, GPIO.OUT)
GPIO.setup(ln1_right, GPIO.OUT)
GPIO.setup(ln2_right, GPIO.OUT)
GPIO.setup(enA_right, GPIO.OUT)
GPIO.setup(ln3_right, GPIO.OUT)
GPIO.setup(ln4_right, GPIO.OUT)
GPIO.setup(enB_right, GPIO.OUT)

#pwm핀 총 4개
enA_left_pwm=GPIO.PWM(enA_left, 100)   #(pin, freq)
enB_left_pwm=GPIO.PWM(enB_left, 100)   #(pin, freq)
enA_right_pwm=GPIO.PWM(enA_right, 100)   #(pin, freq)
enB_right_pwm=GPIO.PWM(enB_right, 100)   #(pin, freq)

enA_left_pwm.start(0)   #(dutycycle)  0 ~ 100
enB_left_pwm.start(0)   #(dutycycle)  0 ~ 100
enA_right_pwm.start(0)   #(dutycycle)  0 ~ 100
enB_right_pwm.start(0)   #(dutycycle)  0 ~ 100

#========================================main task================================
#old_settings = termios.tcgetattr(sys.stdin)
#tty.setcbreak(sys.stdin.fileno())


while(1):
    try:
        #if select.select([sys.stdin], [], [], 0.1)[0]:
            #direction = sys.stdin.read(1)
            
            #기본설정
            
            enA_left_pwm.ChangeDutyCycle(100)
            enB_left_pwm.ChangeDutyCycle(100)
            enA_right_pwm.ChangeDutyCycle(100)
            enA_right_pwm.ChangeDutyCycle(100)
            
            GPIO.output(ln1_left, 0)
            GPIO.output(ln2_left, 0)
            GPIO.output(ln3_left, 0)
            GPIO.output(ln4_left, 0)

            GPIO.output(ln1_right, 0)
            GPIO.output(ln2_right, 0)
            GPIO.output(ln3_right, 0)
            GPIO.output(ln4_right, 0)

            direction=input("((forward:w, backward:s)) : ")

            #전진(4륜구동), 
            if direction=='w' :
                forward_dc()
                
                
            #후진(4륜구동)
            elif direction=='s':
                backward_dc()

            #정지
            elif direction=='d':
                stop_dc()
                
                


    except:
        print("interrupt!!!!!!!!!")
        GPIO.cleanup()
        enA_left_pwm.stop()
        enB_left_pwm.stop()
        enA_right_pwm.stop()
        enB_right_pwm.stop()
        exit(1)
    

#termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)