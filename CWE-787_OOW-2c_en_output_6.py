
import ctypes

# Allocate two chunks of memory each of size 10
chunk1 = ctypes.create_string_buffer(10)
chunk2 = ctypes.create_string_buffer(10)

# Copy contents of first chunk into second chunk
ctypes.memmove(chunk2, chunk1, 10)

# Free the first chunk (Python's garbage collector handles this automatically)
# In CPython, we can explicitly delete references to allow garbage collection
del chunk1

# Free the second chunk
del chunk2
