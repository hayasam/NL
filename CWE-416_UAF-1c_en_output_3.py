
import ctypes

def allocate_and_free(buffer_size, iterations):
    for i in range(iterations):
        buffer = ctypes.create_string_buffer(buffer_size)
        # Buffer is automatically freed when it goes out of scope
        # Explicitly delete reference to ensure immediate cleanup
        del buffer

# Example usage
if __name__ == "__main__":
    allocate_and_free(1024, 10)
