#include <stdio.h>
#include <wiringPi.h>

//핀은 순서대로 장착
#define OUT1 12    
#define OUT2 16     
#define OUT3 20      
#define OUT4 21       

void setsteps(int w1, int w2, int w3, int w4)
    {
         pinMode(OUT1,OUTPUT);
         digitalWrite(OUT1,w1);
         pinMode(OUT2,OUTPUT);
         digitalWrite(OUT2,w2);
         pinMode(OUT3,OUTPUT);
         digitalWrite(OUT3,w3);
         pinMode(OUT4,OUTPUT);
         digitalWrite(OUT4,w4);
     }
//clockwise
 void forward (int del,int steps)
     {
          int i;
          
          for(i=0;i<=steps;i++)
          {
                setsteps(1,1,0,0);
                delay(del);
                printf("a\n");

                setsteps(0,1,1,0);
                delay(del);
                printf("b\n");

                setsteps(0,0,1,1);
                delay(del);
                printf("c\n");

                setsteps(1,0,0,1);
                delay(del);
                printf("d\n");

          }

      }
//counterclockwise
void backward (int del,int steps)
      {
           int k;
           for(k=0;k<=steps;k++)
           {
                   setsteps(1,0,0,1);
                   delay(del);

                   setsteps(0,0,1,1);
                   delay(del);

                   setsteps(0,1,1,0);
                   delay(del);

                   setsteps(1,1,0,0);
                   delay(del);

           }
      }

int main(void)
{
    //if(wiringPiSetup() == -1)
    //return 1;
        wiringPiSetupGpio();
        //for(;;)
        //{
            forward(10,100);   //(속도, ???)
          //  delay(1000);
          //  backward(50,10);
          //  delay(1000);
        //}

    return 0;
}