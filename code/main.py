import thread

from serial_up_worker import SerialUpWorker
from serial_down_worker import SerialDownWorker
from socket_worker import SocketWorker

thread.start_new_thread(SerialUpWorker, ())
thread.start_new_thread(SerialDownWorker, ())
thread.start_new_thread(SocketWorker, ())
