class Config:
    EN_485 = 4
    BAUD_RATE = 19200

    SERIAL_DOWN_CYC = 0.5
    SERIAL_UP_CYC = 0.5

    DOWN_QUEUE_NAME = 'command_queue'
    UP_QUEUE_NAME = 'result_queue'

    SOCKET_HOST = 'ws://127.0.0.1:8080'