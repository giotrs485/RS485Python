import thread

from serial_up_worker import SerialUpWorker
from serial_down_worker import SerialDownWorker
from socket_worker import SocketWorker

thread1 = thread.start_new_thread(SerialUpWorker, ())
thread2 = thread.start_new_thread(SerialDownWorker, ())
thread3 = thread.start_new_thread(SocketWorker, ())

thread1.join()
thread2.join()
thread3.join()