
import sys

def scan(fmt):
    if fmt != "%s\n":
        return 0
    
    buffer = sys.stdin.readline()
    if not buffer:
        return 0
    
    if buffer.endswith('\n'):
        buffer = buffer[:-1]
    
    count = len(buffer)
    sys.stdin.buffer.write(buffer.encode())
    
    return count

def scanf(fmt, buf):
    if fmt != "%s\n":
        return 0
    
    line = sys.stdin.readline()
    if not line:
        return 0
    
    if line.endswith('\n'):
        line = line[:-1]
    
    if len(line) >= 1024:
        line = line[:1023]
    
    buf[0] = line
    return len(line)
