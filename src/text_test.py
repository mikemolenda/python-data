# Test various decoding error handling

x = bytes([65, 66, 67, 255, 192, 193])
# print(x.decode(errors='strict'))
print(x.decode(errors='ignore'))
print(x.decode(errors='replace'))
# print(x.decode(errors='surrogateescape'))
print(x.decode(errors='backslashreplace'))