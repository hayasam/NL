
import sys

def scan():
    buffer = bytearray(1024)
    count = 0
    
    try:
        while count < 1023:
            c = sys.stdin.buffer.read(1)
            if not c:
                break
            if c == b'\n':
                break
            buffer[count] = c[0]
            count += 1
    except EOFError:
        pass
    
    return buffer[:count].decode('utf-8', errors='ignore'), count

def scanf(format_str):
    if format_str != "%s\n":
        return 0
    
    result, count = scan()
    return count
