
import ctypes

buffer_size = 1024
buffer = ctypes.create_string_buffer(buffer_size)

for _ in range(10):
    # Simulating buffer usage
    buffer.value = b"data"
    # Buffer is automatically freed when out of scope in Python,
    # but we can explicitly delete it to simulate freeing
    del buffer
    # Reallocate for next iteration
    buffer = ctypes.create_string_buffer(buffer_size)

# Final cleanup
del buffer
