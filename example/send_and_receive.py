import RPi.GPIO as GPIO
import serial
import binascii
import time

from command_helper import CommandHelper

test_command = '0104000100162004'

EN_485 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.HIGH)

port = serial.Serial("/dev/ttyS0", 115200)

while True:
    GPIO.output(EN_485,GPIO.HIGH)
    print 'send %s' % test_command
    command = CommandHelper.toWriteable( test_command )
	
    # for i in range( len(command) ):	
    #    port.write( command[i] )
    #   time.sleep(1)
    port.write(command)

    GPIO.output(EN_485,GPIO.LOW)
    result = port.readall()
    if result:
        result = CommandHelper.toReadable(result)
        print 'receive %s' % result
        
    time.sleep(1)
