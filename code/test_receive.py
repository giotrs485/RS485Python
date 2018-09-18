import RPi.GPIO as GPIO
import serial

from config import Config

def hex2Str(argv):
    result = ''   
    hLen = len(argv)
    print hLen   
    for i in xrange(hLen):   
        hvol = ord(argv[i])   
        hhex = '%02x'%hvol   
        result += hhex+' '   
    return result 

def str2Hex(str):
    str = str.replace(' ', '')
    hex_values = ['0x' + str[i:i+2] for i in range(0, len(str), 2)]
    int_values = [int(h, base=16) for h in hex_values]
    return int_values

EN_485 = Config.EN_485
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

class Test:
	def __init__(self):
		self.secr = serial.Serial("/dev/ttyS0", Config.BAUD_RATE, timeout=Config.SERIAL_UP_CYC)
		self.start()
	
	def start(self):    
		while True:
			self.executeTask()

	def executeTask(self):
		result = self.secr.readall()
		if result:
			result = hex2Str(result)
			print 'get %s' % result
