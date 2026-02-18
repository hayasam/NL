
import ctypes

def allocate_and_free(buffer_size, loop_count):
    for i in range(loop_count):
        buffer = ctypes.create_string_buffer(buffer_size)
        # Buffer is automatically freed when it goes out of scope
        # Explicitly delete reference to ensure immediate cleanup
        del buffer

if __name__ == "__main__":
    buffer_size = 1024
    loop_count = 10
    allocate_and_free(buffer_size, loop_count)
