import struct

class CommandHelper(object):

    @staticmethod
    def toWriteable( command ):
        arr = []
        command = command.replace(' ', '')
        for i in range(0, len(command), 2):
            int_val = int( command[i:i+2], 16 )
            byte_val = chr( int_val )
            arr.append(byte_val)
        return arr
    
    @staticmethod
    def toReadable( command ):
        print len(command)
        for i in range(len(command)):
            print command[i]
            struct.unpack("h", command[i])
            # print int(command[i], 16)
        # command = bytes.fromhex(command)
        return command