
import ctypes

def memcpy(dest, src, n):
    ctypes.memmove(dest, src, n)

def strlen(s):
    return len(s)

def copy_message_to_buffer(buffer, message):
    message_bytes = message.encode('utf-8')
    length = strlen(message_bytes)
    if len(buffer) >= length:
        memcpy(buffer, message_bytes, length)
        return length
    else:
        return -1
