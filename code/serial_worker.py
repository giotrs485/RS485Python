import RPi.GPIO as GPIO
import serial
import time
import datetime

from config import Config
from command_helper import CommandHelper
from redis_queue import RedisQueue
from binascii import unhexlify

GPIO.setmode(GPIO.BCM)
GPIO.setup(Config.EN_485, GPIO.OUT)
GPIO.output(Config.EN_485, GPIO.HIGH)

DEFAULT_COMMAND = '01 04 00 00 00 46 71 F8'
DEFAULT_COMMAND2 = '01 04 80 00 00 23 98 13'

class SerialWorker:
    def __init__(self):
        self.trigger = False
        self.result_queue = RedisQueue(Config.UP_QUEUE_NAME)
        self.command_queue = RedisQueue(Config.DOWN_QUEUE_NAME)
        self.port = serial.Serial("/dev/ttyS0", 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = Config.SERIAL_WAIT)
        self.start()
    
    def start(self):
        while True:
            self.executeTask()
            time.sleep(Config.SERIAL_CYC)

    def executeTask(self):
        GPIO.output(Config.EN_485,GPIO.HIGH)

        command = self.command_queue.get_nowait()
        if not command:
            self.trigger = not self.trigger
            if self.trigger:
                command = DEFAULT_COMMAND
            else:
                command = DEFAULT_COMMAND2
        
        print 'write to 485 %s' % command

        command = CommandHelper.toWriteable( command )
        self.port.write(command)

        while self.port.out_waiting > 0:
            time.sleep(0.01)

        GPIO.output(Config.EN_485,GPIO.LOW)
        result = self.port.readall()

        if result:
            result = CommandHelper.toReadable(result)
            print 'receive from 485 %s' % result
            self.result_queue.put(result)

if __name__ == "__main__":
    SerialWorker()
    print 'serial worker weak up at %s' % datetime.date.today()
    
