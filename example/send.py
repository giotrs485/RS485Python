# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial
import binascii
import time

def hexShow(argv):   
    result = ''   
    hLen = len(argv)
    print hLen   
    for i in xrange(hLen):   
        hvol = ord(argv[i])   
        hhex = '%02x'%hvol   
        result += hhex+' '   
    return result 

def str2hex(str):
    s=binascii.unhexlify(str)
    b=[ord(x) for x in s]
    return b

EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

ser = serial.Serial("/dev/ttyS0",19200,timeout=1)    
# print t.portstr    
# strInput = raw_input('enter some words:')    
# n = t.write(strInput)    
# print n    
# str = t.read(n)    
# print str   

while True:
    print 'listen'
    str = ser.readall()
    # str = raw_input('enter some words:')
    if str:
        str = hexShow(str)
        print 'get %s' % str
        # str = str2hex(str)
	# str = bytearray.fromhex(str)
	print 'send %s' % str
        # ser.write(serial.to_bytes(str))
	ser.write(str)
	time.sleep(10)
    else:
	    print 'no input'    

