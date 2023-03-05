import RPi.GPIO as GPIO
import time

in1 = 12
in2 = 16
in3 = 20
in4 = 21

def setsteps(w1, w2, w3, w4) :
    
    
    GPIO.output( in1, w1 )
    GPIO.output( in2, w2 )
    GPIO.output( in3, w3)
    GPIO.output( in4, w4 )



#clockwise
def forward (delay,steps) :
    i=0
    
    for i in range(steps) :
          
        setsteps(1,1,0,0)
        time.sleep(delay)

        setsteps(0,1,1,0)
        time.sleep(delay)

        setsteps(0,0,1,1)
        time.sleep(delay)
                
        setsteps(1,0,0,1)
        time.sleep(delay)
                

#counterclockwise
def backward (delay,steps) :

    k=0
    for k in range(steps) :
           
        setsteps(1,0,0,1)
        time.sleep(delay)

        setsteps(0,0,1,1)
        time.sleep(delay)          

        setsteps(0,1,1,0)
        time.sleep(delay)          

        setsteps(1,1,0,0)
        time.sleep(delay)
           


# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings(False)
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )

def cleanup():
    GPIO.output( in1, 0 )
    GPIO.output( in2, 0 )
    GPIO.output( in3, 0 )
    GPIO.output( in4, 0 )
    GPIO.cleanup()

#========================================main task======================================

while True:
    try :    
       
        angle=0
        direction=0

        angle, direction = input("write an angle and direction(CW=1 OR CCW=-1):").split(" ")
        
            
        #clockwise
        if direction==1 and angle>0 :
            forward(0.002, 1.4444*angle)   #(속도, 스텝 수)
            time.sleep(1)
            print("clockwise")
        
        #counterclockwise
        elif direction==-1 and angle>0 :
            backward(0.002, 1.4444*angle)   #(속도, 스텝 수)
            time.sleep(1)
            print("counterclockwise")
        

        else :
            print("please write direction again!!!!!")
        
  
    except KeyboardInterrupt:
        cleanup()
        exit( 1 )

