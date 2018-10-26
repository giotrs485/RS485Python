import RPi.GPIO as GPIO
import serial
import binascii
import time

from command_helper import CommandHelper

test_command = '01 04 00 01 00 16 20 04'

EN_485 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.HIGH)

port = serial.Serial("/dev/ttyS0", 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout=1)

while True:
    GPIO.output(EN_485,GPIO.HIGH)
    print 'send %s' % test_command
    command = CommandHelper.toWriteable( test_command )
    port.write(command)

    while port.out_waiting > 0:
        print '%s waiting' % port.out_waiting
        time.sleep(0.02)

    GPIO.output(EN_485,GPIO.LOW)
    result = port.readall()
    if result:
        result = CommandHelper.toReadable(result)
        print 'receive %s' % result

    time.sleep(0.5)
