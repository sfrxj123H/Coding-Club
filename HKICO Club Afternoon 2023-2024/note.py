import struct

# Binary
text = input("Insert text")
type = input("t for text, n for num")
if type == "t":
    print(' '.join(format(ord(char), '08b') for char in text))
elif type == "n":
    float_number = int(text)
    packed = struct.pack('!f', float_number)
    integer_value = struct.unpack('!I', packed)[0]
    binary_representation = bin(integer_value)[2:].zfill(32)
    print(binary_representation)
