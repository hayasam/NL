
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <buffer_size>")
        sys.exit(1)
    
    try:
        buffer_size = int(sys.argv[1])
        if buffer_size < 0:
            print("Buffer size must be non-negative")
            sys.exit(1)
    except ValueError:
        print("Buffer size must be an integer")
        sys.exit(1)
    
    buffer = bytearray(buffer_size)
    
    for i in range(buffer_size):
        print(f"buffer[{i}] = {buffer[i]}")
    
    sys.exit(0)

if __name__ == "__main__":
    main()
