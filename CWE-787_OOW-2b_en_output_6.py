
import ctypes

# Allocate two chunks of memory each of size 10
chunk1 = (ctypes.c_char * 10)()
chunk2 = (ctypes.c_char * 10)()

# Initialize first chunk with some data
for i in range(10):
    chunk1[i] = bytes([65 + i])  # A, B, C, ...

# Copy contents of first chunk into second chunk
ctypes.memmove(chunk2, chunk1, 10)

# Print contents of the second chunk
print(bytes(chunk2).decode('ascii'))

# Free memory allocated to the first chunk
# In Python, we can't explicitly free ctypes arrays, but we can delete references
del chunk1

# Print contents of the second chunk
print(bytes(chunk2).decode('ascii'))

# Free memory allocated to the second chunk
del chunk2
