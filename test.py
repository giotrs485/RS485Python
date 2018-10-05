command = '00AABBFF'
arr = []
for i in range(0, len(command), 2):
    int_val = int( command[i:i+2], 16 )
    print int_val
    byte_val = chr( int_val )
    print byte_val
    arr.append(byte_val)

print arr
# for i in range(0, len(command), 2):
#     byte = chr( int (command[i:i+2], 16 )

