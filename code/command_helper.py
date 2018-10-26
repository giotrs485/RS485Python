class CommandHelper(object):

    @staticmethod
    def toWriteable( command ):
        arr = []
        command = command.replace(' ', '')
        for i in range(0, len(command), 2):
            int_val = int( command[i:i+2], 16 )
            byte_val = chr( int_val )
            arr.append(byte_val)
        # return ''.join(arr)
        return arr
    
    @staticmethod
    def toReadable( command ):
        result = ''   
        hLen = len(command) 
        for i in xrange(hLen):   
            hvol = ord(command[i])   
            hhex = '%02x'%hvol   
            result += hhex+' '   
        return result 
