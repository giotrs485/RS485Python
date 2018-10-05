import RPi.GPIO as GPIO
import serial
import binascii
import time

from command_helper import CommandHelper

test_command = '00 AA BB CC FF'

# def hex2Str(argv):
#     result = ''   
#     hLen = len(argv)
#     print hLen   
#     for i in xrange(hLen):   
#         hvol = ord(argv[i])   
#         hhex = '%02x'%hvol   
#         result += hhex+' '   
#     return result 

# def str2Hex(str):
#     str = str.replace(' ', '')
#     hex_values = ['0x' + str[i:i+2] for i in range(0, len(str), 2)]
#     int_values = [int(h, base=16) for h in hex_values]
#     return int_values

# def toWriteable( command ):
#     arr = []
#     command = command.replace(' ', '')
#     for i in range(0, len(command), 2):
#         int_val = int( command[i:i+2], 16 )
#         print int_val
#         byte_val = chr( int_val )
#         print byte_val
#         arr.append(byte_val)
#     return arr

EN_485 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

port = serial.Serial("/dev/ttyS0",115200,timeout=1)

while True:
    GPIO.output(EN_485,GPIO.LOW)
    result = port.readall()
    if result:
        result = CommandHelper.toReadable(result)
        print 'receive %s' % result
        GPIO.output(EN_485,GPIO.HIGH)
        port.write( CommandHelper.toWriteable(test_command) )
        print 'send 00'
    time.sleep(0.5)
