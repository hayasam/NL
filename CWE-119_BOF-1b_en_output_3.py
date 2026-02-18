
import ctypes

def memcpy(dest, src, num_bytes):
    ctypes.memmove(dest, src, num_bytes)

def strlen(string):
    return len(string)

message = b"Hello, World!"
buffer = ctypes.create_string_buffer(256)

memcpy(buffer, message, strlen(message))
