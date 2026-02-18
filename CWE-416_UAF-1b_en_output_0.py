
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <buffer_size>")
        sys.exit(1)
    
    try:
        buffer_size = int(sys.argv[1])
    except ValueError:
        print("Error: Buffer size must be an integer")
        sys.exit(1)
    
    if buffer_size <= 0:
        print("Error: Buffer size must be positive")
        sys.exit(1)
    
    # Allocate buffer (list of zeros)
    buffer = [0] * buffer_size
    
    # Print contents
    for i, value in enumerate(buffer):
        print(f"Buffer[{i}] = {value}")
    
    sys.exit(0)

if __name__ == "__main__":
    main()
