import RPi.GPIO as GPIO
import serial
import time

from config import Config
from redis_queue import RedisQueue

GPIO.setmode(GPIO.BCM)
GPIO.setup(Config.EN_485,GPIO.OUT)

class SerialWorker:
    def __init__(self):
        self.result_queue = RedisQueue(Config.UP_QUEUE_NAME)
        self.command_queue = RedisQueue(Config.DOWN_QUEUE_NAME)
        self.port = serial.Serial("/dev/ttyS0", Config.BAUD_RATE, timeout=Config.SERIAL_WAIT)
        self.start()
    
    def start(self):
        while True:
            self.executeTask()
            time.sleep(Config.SERIAL_CYC)

    def executeTask(self):
        GPIO.output(Config.EN_485,GPIO.HIGH)

        command = self.command_queue.get_nowait()
        if not command:
            command = '0'
        
        command = self.str2Hex(command)
        self.port.write(command)
        print 'write to 485 %s' % command

        GPIO.output(Config.EN_485,GPIO.LOW)
        result = self.port.readall()

        if result:
            result = self.hex2Str(result)
            print 'receive from 485 %s' % result
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

if __name__ == "__main__":
    SerialWorker()
    
