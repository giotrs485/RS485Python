import RPi.GPIO as GPIO
import serial
import binascii
import time

def hex2Str(argv):
    result = ''   
    hLen = len(argv)
    print hLen   
    for i in xrange(hLen):   
        hvol = ord(argv[i])   
        hhex = '%02x'%hvol   
        result += hhex+' '   
    return result 

def str2Hex(str):
    str = str.replace(' ', '')
    hex_values = ['0x' + str[i:i+2] for i in range(0, len(str), 2)]
    int_values = [int(h, base=16) for h in hex_values]
    return int_values

EN_485 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

port = serial.Serial("/dev/ttyS0",19200,timeout=1)

while True:
    GPIO.output(EN_485,GPIO.LOW)
    result = port.readall()
    if result:
        # result = hex2Str(result)
        print 'receive %s' % result
        GPIO.output(EN_485,GPIO.HIGH)
        port.write( str2Hex('11') )
        print 'send 11'
    time.sleep(1)
