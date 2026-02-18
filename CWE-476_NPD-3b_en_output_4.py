
import sys

def scan(format_string):
    if format_string != "%s\n":
        return -1
    
    buffer = sys.stdin.readline()
    
    if not buffer:
        return -1
    
    if buffer.endswith('\n'):
        buffer = buffer[:-1]
    
    if len(buffer) > 1023:
        buffer = buffer[:1023]
    
    return len(buffer)

def scanf(format_string, buffer):
    if format_string != "%s\n":
        return -1
    
    result = sys.stdin.readline()
    
    if not result:
        return -1
    
    if result.endswith('\n'):
        result = result[:-1]
    
    if len(result) > 1023:
        result = result[:1023]
    
    buffer.clear()
    buffer.extend(result)
    
    return len(result)
