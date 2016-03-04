#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT) # pin18 
a=GPIO.PWM(18,50)       # pin18
#GPIO.setup(22,GPIO.OUT) # pin22 
#b=GPIO.PWM(22,50)       # pin22
a.start(3.5)
#b.start(4.5)
#counter = 0
'''
while(counter < 1):
        a.ChangeDutyCycle(8)   #90D
        sleep(0.5)
        GPIO.cleanup()
        sleep(5)
        GPIO.setup(18,GPIO.OUT) # pin18
 #       GPIO.setup(22,GPIO.OUT) # pin22
        a.ChangeDutyCycle(12.5)   #180D
        sleep(1)
        a.ChangeDutyCycle(3.5)   #0D
        sleep(1)
        counter = counter + 1

a.ChangeDutyCycle(4.5)   #90D
'''
sleep(0.5)
GPIO.cleanup()

print "bye bye"