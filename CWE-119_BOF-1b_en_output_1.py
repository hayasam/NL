
import ctypes

def mem_copy(dest, src, num_bytes):
    ctypes.memmove(dest, src, num_bytes)

def string_length(s):
    return len(s.encode('utf-8'))

def copy_message_to_buffer(buffer, message):
    message_bytes = message.encode('utf-8')
    mem_copy(buffer, message_bytes, len(message_bytes))
