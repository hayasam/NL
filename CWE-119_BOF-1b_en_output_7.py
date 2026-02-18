
import ctypes

def memcpy(dest, src, n):
    ctypes.memmove(dest, src, n)

def strlen(s):
    return len(s)

def copy_message_to_buffer(buffer, message):
    length = strlen(message)
    memcpy(buffer, message, length)
    return buffer
