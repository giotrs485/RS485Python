import websocket
import thread
import time

from config import Config 
from redis_queue import RedisQueue
from websocket import create_connection, WebSocket

websocket.enableTrace(True)
HOST = Config.SOCKET_HOST

class SocketWorker:
    def __init__(self):
        self.command_queue = RedisQueue(Config.DOWN_QUEUE_NAME)
        self.result_queue = RedisQueue(Config.UP_QUEUE_NAME)
        
        self.socket = websocket.WebSocketApp( 
            HOST, 
            on_open = self.on_open,
            on_message = self.on_message,
            on_error = self.on_error,
            on_close = self.on_close
        )

        while True:
            try:
                self.socket.run_forever(ping_interval=100)
            except:
                pass
            time.sleep(5)
    
    def on_open(self):
        print 'socket connected'
        thread.start_new_thread(self.start, ())

    def on_error(self, error):
        print 'socket error %s' % error


    def on_message(self, message):
        print 'socket get command %s' % message
        self.command_queue.put(message)

    def on_close(self):
        print 'socket close'
    
    def start(self):
        while True:
            self.execTask()
            time.sleep(0.5)
    
    def execTask(self):
        result = self.result_queue.get_nowait()
        if result:
            print 'socket send result %s' % result
            self.socket.send(result)
        

if __name__ == "__main__":
    SocketWorker()
    