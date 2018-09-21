from threading import Thread
from serial_up_worker import SerialUpWorker
from serial_down_worker import SerialDownWorker
from socket_worker import SocketWorker

thread1 = Thread(target=SerialUpWorker)
thread2 = Thread(target=SerialDownWorker)
thread3 = Thread(target=SocketWorker)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
