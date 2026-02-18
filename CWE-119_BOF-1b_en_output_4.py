
import ctypes

def memcpy(dest, src, num_bytes):
    ctypes.memmove(dest, src, num_bytes)

def strlen(string):
    return len(string)

message = b"Hello, World!"
buffer_size = 100
buffer = ctypes.create_string_buffer(buffer_size)

memcpy(buffer, message, strlen(message))
