
import ctypes

def memcpy(dest, src, n):
    ctypes.memmove(dest, src, n)

def strlen(string):
    return len(string)

buffer = ctypes.create_string_buffer(10)
src_string = b"Hello"
memcpy(buffer, src_string, strlen(src_string))
