
import ctypes

def memcpy(dest, src, num_bytes):
    ctypes.memmove(dest, src, num_bytes)

def strlen(string):
    return len(string)

def copy_message_to_buffer(buffer, message):
    message_bytes = message.encode('utf-8')
    memcpy(buffer, message_bytes, len(message_bytes))
