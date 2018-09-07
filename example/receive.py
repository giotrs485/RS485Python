# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial

import serial.tools.list_ports
plist = list(serial.tools.list_ports.comports())
for port in list( plist ):
    print port

EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

ser = serial.Serial("/dev/ttyS0",115200,timeout=1)  # open first serial port    
while 1:  
    str = ser.readall()  
    if str:  
        print str 
