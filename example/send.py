# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial

EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

ser = serial.Serial("/dev/ttyS0",9600,timeout=0.5)    
# print t.portstr    
# strInput = raw_input('enter some words:')    
# n = t.write(strInput)    
# print n    
# str = t.read(n)    
# print str   

while True:
    print ser.portstr
    str = ser.readall()
    print str 
    # str = raw_input('enter some words:')
    if str:
	print 'get %s' % str
	print type(str)
	f = open('res.txt', 'a')
	f.write(str)
	f.close()
        n = ser.write(str)
    else:
	print 'no input'    

