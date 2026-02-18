
import ctypes

# Allocate two chunks of memory each of size 10
chunk1 = (ctypes.c_char * 10)()
chunk2 = (ctypes.c_char * 10)()

# Copy contents of first chunk into second chunk
ctypes.memmove(chunk2, chunk1, 10)

# Print contents of second chunk
print(bytes(chunk2).hex())

# Free memory allocated to first chunk
del chunk1

# Print contents of second chunk
print(bytes(chunk2).hex())

# Free memory allocated to second chunk
del chunk2
