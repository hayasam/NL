
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <buffer_size>")
        sys.exit(1)
    
    try:
        buffer_size = int(sys.argv[1])
        if buffer_size < 0:
            raise ValueError("Buffer size must be non-negative")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    buffer = bytearray(buffer_size)
    
    for i, byte in enumerate(buffer):
        print(f"buffer[{i}] = {byte}")
    
    sys.exit(0)

if __name__ == "__main__":
    main()
