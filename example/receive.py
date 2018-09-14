# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial

EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

ser = serial.Serial("/dev/ttyS0",19200,timeout=1)   
while True:  
    str = ser.readall()  
    if str:  
        print str
        ser.write('res for ' + str)

