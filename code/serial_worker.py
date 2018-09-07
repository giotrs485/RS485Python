from datetime import datetime
from redis_queue import RedisQueue

import time

# EN_485 =  4
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(EN_485,GPIO.OUT)
# GPIO.output(EN_485,GPIO.LOW)

class SerialWorker:
    def __init__(self):
        # self.ser = serial.Serial("/dev/ttyS0",115200,timeout=1)
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
            print 'command %s ' % command
            # self.secr.write(command)
        else:
            print 'simple'
            # self.secr.write('simple request here')
        
        # result = self.secr.readall()
        result = ''
        if result:
            print 'result %s ' % result
            # self.result_queue.put(result)
        else:
            print 'no result'
    