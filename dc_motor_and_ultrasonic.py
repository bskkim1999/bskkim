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
enA_front=0
ln1_front=5
ln2_front=6

#왼쪽 앞바퀴
enB_front=22
ln3_front=17
ln4_front=27

#<<초음파센서>>
#전방(가운데)
GPIO_TRIGGER_mid = 18
GPIO_ECHO_mid = 15

#왼쪽
GPIO_TRIGGER_left=23
GPIO_ECHO_left=24

#오른쪽
GPIO_TRIGGER_right=16
GPIO_ECHO_right=12


#======================================function==========================================================
#dutycycle : 0 ~ 100
#앞으로가기
def dc_rightback(dutycycle):
    
    enA_pwm_back.ChangeDutyCycle(dutycycle)

    #앞으로가기
    GPIO.output(ln1_back, 0)
    GPIO.output(ln2_back, 1)

    return None

def dc_leftback(dutycycle):
    
    enB_pwm_back.ChangeDutyCycle(dutycycle)

    #앞으로가기
    GPIO.output(ln3_back, 1)
    GPIO.output(ln4_back, 0)

    return None

def dc_leftfront(dutycycle):
    enB_pwm_front.ChangeDutyCycle(dutycycle)

    #앞으로가기
    GPIO.output(ln3_front, 1)
    GPIO.output(ln4_front, 0)

    return None

def dc_rightfront(dutycycle):
    enA_pwm_front.ChangeDutyCycle(dutycycle)

    #앞으로가기
    GPIO.output(ln1_front, 1)
    GPIO.output(ln2_front, 0)

    return None
#--------------------------------------------
#뒤로가기
def dc_rightback_backup(dutycycle):
    
    enA_pwm_back.ChangeDutyCycle(dutycycle)

    #뒤로가기
    GPIO.output(ln1_back, 1)
    GPIO.output(ln2_back, 0)

    return None

def dc_leftback_backup(dutycycle):
    
    enB_pwm_back.ChangeDutyCycle(dutycycle)

    #뒤로가기
    GPIO.output(ln3_back, 0)
    GPIO.output(ln4_back, 1)

    return None

def dc_leftfront_backup(dutycycle):
    enB_pwm_front.ChangeDutyCycle(dutycycle)

    #뒤로가기
    GPIO.output(ln3_front, 0)
    GPIO.output(ln4_front, 1)

    return None

def dc_rightfront_backup(dutycycle):
    enA_pwm_front.ChangeDutyCycle(dutycycle)

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
    GPIO.output(ln4_back, 0)
#-----------------------------------------------
#초음파센서
#전방(가운데)
def distance_mid():
    # set Trigger to HIGH
    print("distance_mid function start!!")
    GPIO.output(GPIO_TRIGGER_mid, 1)
    
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_mid, 0)
 
    StartTime = time.time()
    StopTime = time.time()
    
    # save StartTime
    while GPIO.input(GPIO_ECHO_mid) == 0:
        StartTime = time.time()
       
    
    # save time of arrival
    while GPIO.input(GPIO_ECHO_mid) == 1:
        StopTime = time.time()
        
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance1 = (TimeElapsed * 34300) / 2
    #print ("Measured Distance = %.1f cm" % distance2)
    print("distance_mid function finish!!")
    return distance1

#왼쪽 초음파센서
def distance_left():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_left, 1)
    
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_left, 0)
 
    StartTime = time.time()
    StopTime = time.time()
    
    # save StartTime
    while GPIO.input(GPIO_ECHO_left) == 0:
        StartTime = time.time()
       
    
    # save time of arrival
    while GPIO.input(GPIO_ECHO_left) == 1:
        StopTime = time.time()
        
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance2 = (TimeElapsed * 34300) / 2
    #print ("Measured Distance = %.1f cm" % distance2)
    print("distance_left function finish!!")
    return distance2

#오른쪽 초음파센서
def distance_right():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_right, 1)
    
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_right, 0)
 
    StartTime = time.time()
    StopTime = time.time()
    
    # save StartTime
    while GPIO.input(GPIO_ECHO_right) == 0:
        StartTime = time.time()
       
    
    # save time of arrival
    while GPIO.input(GPIO_ECHO_right) == 1:
        StopTime = time.time()
        
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance3 = (TimeElapsed * 34300) / 2
    #print ("Measured Distance = %.1f cm" % distance2)
    print("distance_right function finish!!")

    return distance3

#----------------------------------------------
#중앙값 찾기
def find_median():
    print("find_median function start!!")
    idx=0
    median=0

    list = [0 for i in range(3)] #리스트 길이를 지정하고, 0으로 초기화함.
    
    #리스트에 거리값을 대입한다.
    for j in range(len(list)):
        
        tmp=distance_mid()
        list[j]=tmp
        time.sleep(0.01)
        
    
    #자료를 오름차순으로 정렬한다.
    list.sort()

    #최종적으로 중앙값을 도출한다.
    idx=len(list)//2
    median=list[idx]
    
    #print ("Measured Distance = %.1f cm" % median)
    print("find_median function finish!!")
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
#mid 가운데 전방
GPIO.setup(GPIO_TRIGGER_mid, GPIO.OUT)
GPIO.setup(GPIO_ECHO_mid, GPIO.IN)
#left 왼쪽
GPIO.setup(GPIO_TRIGGER_left, GPIO.OUT)
GPIO.setup(GPIO_ECHO_left, GPIO.IN)

#right 오른쪽
GPIO.setup(GPIO_TRIGGER_right, GPIO.OUT)
GPIO.setup(GPIO_ECHO_right, GPIO.IN)


#--------------------------------------
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
        print("start!!")
        
        mid=find_median()
        left=distance_left()
        right=distance_right()
        wherego=0
        #print("abc")
        
        print ("Mid = %.1f cm" % mid, end=" " )
        print ("left = %.1f cm" % left, end=" " )
        print ("right = %.1f cm" % right )
        
        
        if mid<=30.0:
            print("under 30cm!!")
            dc_stop()
            """
            #방향판단
            if left<right:
                wherego=1

            else:
                wherego=-1

            #멈춘다.
            dc_stop()
            time.sleep(1) #1초
            """
            """"
            #후진한다.
            dc_rightback_backup(70)
            dc_leftback_backup(70)
            dc_leftfront_backup(70)
            dc_rightfront_backup(70)
            time.sleep(0.7)  #0.7초
            
            print("{}".format(wherego))
            if wherego== 1:
                #오른쪽으로 튼다.
                dc_leftfront(100)
                dc_leftback(100)
                dc_rightfront_backup(100)
                dc_rightback_backup(100)
                time.sleep(0.7)  #1초
            
            else:
                #왼쪽으로 튼다.
                dc_leftback_backup(100)
                dc_leftfront_backup(100)
                dc_rightfront(100)
                dc_rightback(100)
                time.sleep(0.7)  #1초
            """    

        else:
            #전진한다.
            dc_rightback(100)
            dc_leftback(100)
            dc_leftfront(100)
            dc_rightfront(100)
        
        time.sleep(0.2)

    except KeyboardInterrupt:
        print("interrupt!!!!!!!!!")
        GPIO.cleanup()
        #실험결과, cleanup()함수호출을 통해서 pwm종료가 가능하다.
        enA_pwm_back.stop()
        enB_pwm_back.stop()
        enA_pwm_front.stop()
        enB_pwm_front.stop()
        exit(1)
