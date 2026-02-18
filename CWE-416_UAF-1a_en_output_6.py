
import ctypes

def create_buffer(buffer_size):
    buffer = (ctypes.c_char * buffer_size)()
    for i in range(buffer_size):
        buffer[i] = b'A'
    return buffer
