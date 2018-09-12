import RPi.GPIO as GPIO
import serial

from datetime import datetime
from redis_queue import RedisQueue

import time

EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

class SerialWorker:
    def __init__(self):
        self.secr = serial.Serial("/dev/ttyS0",115200,timeout=1)
        self.command_queue = RedisQueue('command_queue')
        self.result_queue = RedisQueue('result_queue')
        self.start()
    
    def start(self):
        while True:
            self.execTask()
            time.sleep(0.5)
    
    def execTask(self):
        command = self.command_queue.get_nowait()
        if command:
            # write server command
            print 'get server command %s, execute' % command
            command = self.str2Hex(command)
        else:
            # write normal check command
            print 'no command, query'
            command = self.str2Hex('0000000000')

        self.secr.write( serial.to_bytes(command) )
        result = self.secr.readall()

        if result:
            # return result
            print 'get result %s' % result
            self.result_queue.put(result)
    
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
        
        

