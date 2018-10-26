import RPi.GPIO as GPIO
import serial
import time

from config import Config
from command_helper import CommandHelper
from redis_queue import RedisQueue
from binascii import unhexlify

GPIO.setmode(GPIO.BCM)
GPIO.setup(Config.EN_485, GPIO.OUT)
GPIO.output(Config.EN_485, GPIO.HIGH)

DEFAULT_COMMAND = '01 04 00 01 00 16 20 04'

class SerialWorker:
    def __init__(self):
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
            command = DEFAULT_COMMAND
        
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
    
