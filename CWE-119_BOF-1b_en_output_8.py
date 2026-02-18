
import ctypes

def memcpy(dest, src, n):
    ctypes.memmove(dest, src, n)

def strlen(s):
    return len(s)

message = b"Hello, World!"
buffer = ctypes.create_string_buffer(256)

memcpy(buffer, message, strlen(message))
