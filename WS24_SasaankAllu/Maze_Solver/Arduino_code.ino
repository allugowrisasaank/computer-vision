#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;
int p[] = {0, 100, 0, 100, 1, 100, 1, 100, 0, 100, 3, 100, 3, 100, 0, 100, 1, 100, 1, 100, 0, 100, 3, 100,0,0,0,0,0,0};
volatile int i=-2;
float gyroXOffset = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(4,INPUT);
  Wire.begin();
  mpu.initialize();
  pinMode(7,OUTPUT);//l
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);//r
  pinMode(10,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    
    bool glow = digitalRead(4);    
      i=i+2;
      int16_t ax, ay, az, gx=gyroXOffset, gy, gz;
      while((gx-gyroXOffset)<(p[i]*90)){
        digitalWrite(7,HIGH);
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,HIGH);
        delay(100);
        digitalWrite(7,LOW);
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
        digitalWrite(10,LOW);       
      mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
      } 
      gyroXOffset += gx;
      //reset total turn to 0;
        do{
          digitalWrite(7,HIGH);
        digitalWrite(8,LOW);
        digitalWrite(9,HIGH);
        digitalWrite(10,LOW);
        delay(100);
        bool glow = digitalRead(4);    
        } 
       while(glow==1);   
  }

