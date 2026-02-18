
import sys

def main():
    # First allocation
    buf = bytearray(1024)
    
    # Read first 100 characters from stdin
    data1 = sys.stdin.read(100)
    if len(data1) > 0:
        buf[:len(data1)] = data1.encode()
    
    # Second allocation
    buf1 = bytearray(1024)
    
    # Read second 100 characters from stdin
    data2 = sys.stdin.read(100)
    if len(data2) > 0:
        buf1[:len(data2)] = data2.encode()
    
    # Alternative using fgets-like behavior
    # Reset for fgets example
    buf_fgets = bytearray(1024)
    
    # Simulating fgets reading up to 1024 characters
    line = sys.stdin.readline()
    if line:
        # Copy up to min(len(line), 1024) bytes
        copy_len = min(len(line), 1024)
        buf_fgets[:copy_len] = line[:copy_len].encode()

if __name__ == "__main__":
    main()
