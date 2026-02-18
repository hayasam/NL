
import ctypes
import sys

def allocate_and_free(buffer_size, iterations):
    for i in range(iterations):
        # Allocate buffer
        buffer = ctypes.create_string_buffer(buffer_size)
        
        # Simulate some usage
        buffer.raw = b'X' * buffer_size
        
        # Buffer is automatically freed when it goes out of scope
        # Explicitly delete reference to ensure immediate cleanup
        del buffer

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <buffer_size> <iterations>")
        sys.exit(1)
    
    try:
        buffer_size = int(sys.argv[1])
        iterations = int(sys.argv[2])
        
        if buffer_size <= 0 or iterations <= 0:
            raise ValueError("Values must be positive integers")
            
        allocate_and_free(buffer_size, iterations)
        print(f"Allocated and freed buffer of size {buffer_size} {iterations} times")
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
