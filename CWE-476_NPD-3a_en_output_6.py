
import sys

def main():
    # First allocation
    buf = bytearray(1024)
    
    # Read up to 100 characters from stdin into first buffer
    data1 = sys.stdin.read(100)
    if data1:
        buf[:len(data1)] = data1.encode()
    
    # Second allocation
    buf1 = bytearray(1024)
    
    # Read up to 100 characters from stdin into second buffer
    data2 = sys.stdin.read(100)
    if data2:
        buf1[:len(data2)] = data2.encode()
    
    # Optional: Print the contents to verify
    print("Buffer 1:", buf[:100].decode('utf-8', errors='ignore'))
    print("Buffer 2:", buf1[:100].decode('utf-8', errors='ignore'))

if __name__ == "__main__":
    main()
