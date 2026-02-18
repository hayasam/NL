
import sys

def scan(format_str):
    if format_str != "%s\n":
        return -1
    
    buffer = sys.stdin.readline()
    
    if not buffer:
        return 0
    
    if buffer.endswith('\n'):
        buffer = buffer[:-1]
    
    if len(buffer) > 1023:
        buffer = buffer[:1023]
    
    return len(buffer)
