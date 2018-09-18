import RPi.GPIO as GPIO
import serial

from config import Config
from redis_queue import RedisQueue

class SerialUpWorker:
  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Config.EN_485,GPIO.OUT)
    GPIO.output(Config.EN_485,GPIO.LOW)
    self.secr = serial.Serial("/dev/ttyS0", Config.BAUD_RATE, timeout=Config.SERIAL_UP_CYC)
    self.result_queue = RedisQueue(Config.UP_QUEUE_NAME)
    self.start()

  def start(self):    
    while True:
      self.executeTask()

  def executeTask(self):
    result = self.secr.readall()
    if result:
      result = self.hex2Str(result)
      print 'get %s' % result
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

