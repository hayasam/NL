
import sys

def first_method():
    buf = bytearray(1024)
    data = sys.stdin.read(100)
    buf[:len(data)] = data.encode()[:100]
    return buf

def second_method():
    buf1 = bytearray(1024)
    data = sys.stdin.read(100)
    buf1[:len(data)] = data.encode()[:100]
    return buf1

if __name__ == "__main__":
    buffer1 = first_method()
    buffer2 = second_method()
