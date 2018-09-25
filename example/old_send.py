# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial

EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.HIGH)

ser = serial.Serial("/dev/ttyS0",19200)

def str2Hex(str):
    str = str.replace(' ', '')
    hex_values = ['0x' + str[i:i+2] for i in range(0, len(str), 2)]
    int_values = [int(h, base=16) for h in hex_values]
    return int_values

while True:
    str = raw_input('enter some words:')
    str = str2Hex(str)
    res = ser.write(str)
    print 'res %s' % res
