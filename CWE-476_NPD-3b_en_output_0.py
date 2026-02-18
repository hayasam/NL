
import sys

def scan(format_string):
    if format_string != "%s\n":
        return -1
    
    buffer = sys.stdin.readline()
    
    if not buffer:
        return -1
    
    if buffer.endswith('\n'):
        buffer = buffer[:-1]
        chars_read = len(buffer) + 1
    else:
        chars_read = len(buffer)
    
    if len(buffer) > 1023:
        buffer = buffer[:1023]
        chars_read = 1024
    
    return chars_read, buffer

def scanf(format_string, buffer):
    result = scan(format_string)
    if result == -1:
        return -1
    
    chars_read, data = result
    buffer[:len(data)] = data.encode()
    buffer[len(data)] = 0
    return chars_read
