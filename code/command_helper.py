
class CommandHelper:
    def toWriteable( command ):
        arr = []
        command = command.replace(' ', '')
        for i in range(0, len(command), 2):
            int_val = int( command[i:i+2], 16 )
            print int_val
            byte_val = chr( int_val )
            print byte_val
            arr.append(byte_val)
        return arr
    
    def toReadable( command ):
        print command
        return command