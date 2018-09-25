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

while True:
    GPIO.setup(EN_485,GPIO.OUT)
    GPIO.output(EN_485,GPIO.LOW)

    receive_serial = serial.Serial("/dev/ttyS0",19200,timeout=1)
    receive_serial.open()
    result = receive_serial.readall()
    receive_serial.close()

    if result:
        result = hex2Str(result)
        print 'receive %s' % result

        GPIO.setup(EN_485,GPIO.OUT)
        GPIO.output(EN_485,GPIO.HIGH)
        
        send_serial = serial.Serial("/dev/ttyS0",19200)
        send_serial.open()
        send_serial.write( str2Hex('11') )
        send_serial.close()

        print 'send 11'
