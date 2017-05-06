# Test decoding a byte array to unicode string

b = [0, 9, 32, 48, 65, 66, 67]
b_string = bytes(b)
print(b_string.decode())
