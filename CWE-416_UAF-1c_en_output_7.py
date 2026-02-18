
import ctypes
import sys

def allocate_and_free(buffer_size, iterations):
    for i in range(iterations):
        # Allocate buffer
        buffer = ctypes.create_string_buffer(buffer_size)
        
        # Simulate some usage
        buffer.raw = b'A' * buffer_size
        
        # Buffer is automatically freed when it goes out of scope
        # Explicitly delete reference to ensure immediate cleanup
        del buffer

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <buffer_size> <iterations>")
        sys.exit(1)
    
    buffer_size = int(sys.argv[1])
    iterations = int(sys.argv[2])
    
    allocate_and_free(buffer_size, iterations)
