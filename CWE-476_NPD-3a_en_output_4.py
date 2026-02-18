
import sys

def main():
    # Allocate first buffer
    buf = bytearray(1024)
    
    # Read up to 100 characters from stdin into first buffer
    input_data = sys.stdin.read(100)
    buf[:len(input_data)] = input_data.encode()
    
    # Allocate second buffer
    buf1 = bytearray(1024)
    
    # Read up to 100 characters from stdin into second buffer
    input_data2 = sys.stdin.read(100)
    buf1[:len(input_data2)] = input_data2.encode()
    
    # Print the contents of both buffers
    print(buf.decode('utf-8', errors='ignore').rstrip('\x00'))
    print(buf1.decode('utf-8', errors='ignore').rstrip('\x00'))

if __name__ == "__main__":
    main()
