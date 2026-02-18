
import sys

def main():
    # Allocate first buffer
    buf = bytearray(1024)
    
    # Read up to 100 characters from stdin into first buffer
    data = sys.stdin.read(100)
    if data:
        buf[:len(data)] = data.encode()
    
    # Allocate second buffer
    buf1 = bytearray(1024)
    
    # Read up to 100 characters from stdin into second buffer
    data = sys.stdin.read(100)
    if data:
        buf1[:len(data)] = data.encode()

if __name__ == "__main__":
    main()
