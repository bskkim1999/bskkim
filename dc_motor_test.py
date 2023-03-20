import RPi.GPIO as GPIO
import time


#================================================================================
#<<핀 헤더 설정>>
##뒷바퀴##
power_right=26
#오른쪽 뒷바퀴
enA_back=14
ln1_back=20
ln2_back=21
#왼쪽 뒷바퀴
enB_back=8
ln3_back=1
ln4_back=7
#-------------------------
##앞바퀴##
power_left=19
#오른쪽 앞바퀴
enA_front=2
ln1_front=3
ln2_front=4

#왼쪽 앞바퀴
enB_front=22
ln3_front=17
ln4_front=27

#=======================================================================================================
#앞으로가기
def dc_rightback():
    
    enA_pwm_back.ChangeDutyCycle(100)

    #앞으로가기
    GPIO.output(ln1_back, 0)
    GPIO.output(ln2_back, 1)

    return None

def dc_leftback():
    
    enB_pwm_back.ChangeDutyCycle(100)

    #앞으로가기
    GPIO.output(ln3_back, 1)
    GPIO.output(ln4_back, 0)

    return None

def dc_leftfront():
    enB_pwm_front.ChangeDutyCycle(100)

    #앞으로가기
    GPIO.output(ln3_front, 1)
    GPIO.output(ln4_front, 0)

    return None

def dc_rightfront():
    enA_pwm_front.ChangeDutyCycle(100)

    #앞으로가기
    GPIO.output(ln1_front, 1)
    GPIO.output(ln2_front, 0)

    return None
#--------------------------------------------
#뒤로가기
def dc_rightback_backup():
    
    enA_pwm_back.ChangeDutyCycle(100)

    #뒤로가기
    GPIO.output(ln1_back, 1)
    GPIO.output(ln2_back, 0)

    return None

def dc_leftback_backup():
    
    enB_pwm_back.ChangeDutyCycle(100)

    #뒤로가기
    GPIO.output(ln3_back, 0)
    GPIO.output(ln4_back, 1)

    return None

def dc_leftfront_backup():
    enB_pwm_front.ChangeDutyCycle(100)

    #뒤로가기
    GPIO.output(ln3_front, 1)
    GPIO.output(ln4_front, 0)

    return None

def dc_rightfront_backup():
    enA_pwm_front.ChangeDutyCycle(100)

    #뒤로가기
    GPIO.output(ln1_front, 0)
    GPIO.output(ln2_front, 1)

    return None


#==================================================================================
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(enA_back, GPIO.OUT)
GPIO.setup(ln1_back, GPIO.OUT)
GPIO.setup(ln2_back, GPIO.OUT)
GPIO.setup(ln3_back, GPIO.OUT)
GPIO.setup(ln4_back, GPIO.OUT)
GPIO.setup(enB_back, GPIO.OUT)
GPIO.setup(power_right, GPIO.OUT)

GPIO.setup(enA_front, GPIO.OUT)
GPIO.setup(ln1_front, GPIO.OUT)
GPIO.setup(ln2_front, GPIO.OUT)
GPIO.setup(ln3_front, GPIO.OUT)
GPIO.setup(ln4_front, GPIO.OUT)
GPIO.setup(enB_front, GPIO.OUT)
GPIO.setup(power_left, GPIO.OUT)


enA_pwm_back=GPIO.PWM(enA_back, 100)
enA_pwm_back.start(0)

enB_pwm_back=GPIO.PWM(enB_back, 100)
enB_pwm_back.start(0)


enA_pwm_front=GPIO.PWM(enA_front, 100)
enA_pwm_front.start(0)


enB_pwm_front=GPIO.PWM(enB_front, 100)
enB_pwm_front.start(0)
#==============================================main task==============================
while True:
    try:
        
        GPIO.output(power_right, 1)
        GPIO.output(power_left, 1)
        
        dc_rightback()
        dc_leftback()
        dc_leftfront()
        dc_rightfront()

        """
        direction=input("write w or s or a: ")
        
        
        if direction=="w":
            dc_rightback()
            dc_leftback()
            dc_leftfront()
            dc_rightfront()

        elif direction=="s":
            dc_rightback_backup()
            dc_leftback_backup()
            dc_leftfront_backup()
            dc_rightfront_backup()

        elif direction=="a":
            dc_leftback_backup()
            dc_leftfront_backup()
            dc_rightfront()
            dc_leftfront()

        """

    except:
        print("interrupt!!!!!!!!!")
        GPIO.cleanup()
        #실험결과, cleanup()함수호출을 통해서 pwm종료가 가능하다.
        #enA_pwm_back.stop()
        #enB_pwm_back.stop()
        #enA_pwm_front.stop()
        #enB_pwm_front.stop()
        exit(1)
