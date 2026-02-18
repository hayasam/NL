
import ctypes

def allocate_and_free(buffer_size, loop_count):
    for i in range(loop_count):
        buffer = ctypes.create_string_buffer(buffer_size)
        # Buffer is automatically freed when it goes out of scope
        # Explicit deletion can be forced
        del buffer

# Example usage
if __name__ == "__main__":
    allocate_and_free(1024, 10)
