# from serial_worker import SerialWorker
from socket_worker import SocketWorker

# SerialWorker()
SocketWorker()

# import serial 

# str = '01 02 03 04 FF'
# str = str.replace(' ', '')
# hex_values = ['0x' + str[i:i+2] for i in range(0, len(str), 2)]
# int_values = [int(h, base=16) for h in hex_values]

# print int_values