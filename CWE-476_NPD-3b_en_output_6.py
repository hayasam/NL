
import sys

def scan():
    buffer = [''] * 1024
    i = 0
    while i < 1023:
        c = sys.stdin.read(1)
        if not c:
            break
        if c == '\n':
            break
        buffer[i] = c
        i += 1
    return ''.join(buffer[:i]), i
