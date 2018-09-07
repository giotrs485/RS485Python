import RPi.GPIO as GPIO
import serial

EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

class SerialConn:
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyS0",115200,timeout=1)
        self.start()
    
    def start():
        