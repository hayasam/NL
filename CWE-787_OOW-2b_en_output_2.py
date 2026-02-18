
import ctypes

# Allocate two chunks of memory each of size 10
first_chunk = (ctypes.c_char * 10)()
second_chunk = (ctypes.c_char * 10)()

# Copy contents of first chunk into second chunk
ctypes.memmove(second_chunk, first_chunk, 10)

# Print contents of second chunk
print("First print:", list(second_chunk))

# Free memory allocated to first chunk
del first_chunk

# Print contents of second chunk again
print("Second print:", list(second_chunk))

# Free memory allocated to second chunk
del second_chunk
