import RPi.GPIO as GPIO
import time


#================================================================================
#<<핀 헤더 설정>>
##뒷바퀴##

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

#오른쪽 앞바퀴
enA_front=2
ln1_front=3
ln2_front=4

#왼쪽 앞바퀴
enB_front=22
ln3_front=17
ln4_front=27

#<<초음파센서>>
GPIO_TRIGGER = 18
GPIO_ECHO = 15

#======================================function==========================================================
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
    GPIO.output(ln3_front, 0)
    GPIO.output(ln4_front, 1)

    return None

def dc_rightfront_backup():
    enA_pwm_front.ChangeDutyCycle(100)

    #뒤로가기
    GPIO.output(ln1_front, 0)
    GPIO.output(ln2_front, 1)

    return None

#정지하기
def dc_stop():
    GPIO.output(ln1_front, 0)
    GPIO.output(ln2_front, 0)
    GPIO.output(ln3_front, 0)
    GPIO.output(ln4_front, 0)
    GPIO.output(ln1_back, 0)
    GPIO.output(ln2_back, 0)
    GPIO.output(ln3_back, 0)
    GPIO.output(ln3_back, 0)
#-----------------------------------------------
#초음파센서
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, 1)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, 0)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance2 = (TimeElapsed * 34300) / 2
 
    return distance2
#----------------------------------------------
#중앙값 찾기
def find_median():
    idx=0
    median=0

    list = [0 for i in range(8)] #리스트 길이를 지정하고, 0으로 초기화함.
    
    #리스트에 거리값을 대입한다.
    for j in range(len(list)):
        print("a")
        tmp=distance()
        list[j]=tmp
        print(list)
        
    
    #자료를 오름차순으로 정렬한다.
    list.sort()

    #최종적으로 중앙값을 도출한다.
    idx=len(list)//2+1
    median=list[idx]
    
    print ("Measured Distance = %.1f cm" % median)

    return median

#=================================setup======================================
#dc모터
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(enA_back, GPIO.OUT)
GPIO.setup(ln1_back, GPIO.OUT)
GPIO.setup(ln2_back, GPIO.OUT)
GPIO.setup(ln3_back, GPIO.OUT)
GPIO.setup(ln4_back, GPIO.OUT)
GPIO.setup(enB_back, GPIO.OUT)

GPIO.setup(enA_front, GPIO.OUT)
GPIO.setup(ln1_front, GPIO.OUT)
GPIO.setup(ln2_front, GPIO.OUT)
GPIO.setup(ln3_front, GPIO.OUT)
GPIO.setup(ln4_front, GPIO.OUT)
GPIO.setup(enB_front, GPIO.OUT)

#초음파센서
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#pwm
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
        
        #전진한다.
        dc_rightback()
        dc_leftback()
        dc_leftfront()
        dc_rightfront()

        if find_median()<=30.0:
            dc_stop()

        time.sleep(0.05)
        print("C")
        

    except:
        print("interrupt!!!!!!!!!")
        GPIO.cleanup()
        #실험결과, cleanup()함수호출을 통해서 pwm종료가 가능하다.
        enA_pwm_back.stop()
        enB_pwm_back.stop()
        enA_pwm_front.stop()
        enB_pwm_front.stop()
        exit(1)
