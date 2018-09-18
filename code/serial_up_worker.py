import RPi.GPIO as GPIO
import serial
import time

from datetime import datetime
from redis_queue import RedisQueue
from config import Config

EN_485 =  Config.EN_485
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

class SerialUpWorker:
    def __init__(self):
        self.secr = serial.Serial("/dev/ttyS0", Config.BAUD_RATE, timeout= 1)
        self.result_queue = RedisQueue(Config.UP_QUEUE_NAME)
        self.start()
    
    def start(self):
        while True:
            self.execTask()
            time.sleep(Config.SERIAL_UP_CYC)
    
    def execTask(self):
        result = self.secr.readall()
        if result:
            print 'get result %s' % result
            self.result_queue.put( self.hex2Str(result) )
        else:
            print 'no result'
    
    def hex2Str(self, argv):
        result = ''   
        hLen = len(argv)
        print hLen   
        for i in xrange(hLen):   
            hvol = ord(argv[i])   
            hhex = '%02x'%hvol   
            result += hhex+' '   
        return result 

    def str2Hex(self, str):
        str = str.replace(' ', '')
        hex_values = ['0x' + str[i:i+2] for i in range(0, len(str), 2)]
        int_values = [int(h, base=16) for h in hex_values]
        return int_values