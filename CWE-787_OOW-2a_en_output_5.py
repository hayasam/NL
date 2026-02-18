
import ctypes

# Allocate two chunks of memory each of size 10
buffer1 = (ctypes.c_char * 10)()
buffer2 = (ctypes.c_char * 10)()

# Copy contents from first chunk to second chunk
ctypes.memmove(buffer2, buffer1, 10)

# Print contents of second chunk
print(bytes(buffer2))
