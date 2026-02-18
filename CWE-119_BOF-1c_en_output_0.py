
import ctypes

def memcpy(dest, src, num_bytes):
    """Copy num_bytes from src to dest memory location."""
    ctypes.memmove(dest, src, num_bytes)

def strlen(string):
    """Return the length of a null-terminated string."""
    length = 0
    while string[length] != '\0':
        length += 1
    return length

# Create source string and destination buffer
src_string = "Hello\0"
buffer_size = 256
dest_buffer = ctypes.create_string_buffer(buffer_size)

# Copy the string
memcpy(dest_buffer, src_string.encode('utf-8'), strlen(src_string) + 1)
