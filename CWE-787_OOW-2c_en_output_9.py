
import ctypes

# Allocate two chunks of memory each of size 10
chunk1 = (ctypes.c_char * 10)()
chunk2 = (ctypes.c_char * 10)()

# Copy contents of first chunk into second chunk
ctypes.memmove(chunk2, chunk1, 10)

# Free the first chunk
del chunk1

# Free the second chunk
del chunk2
