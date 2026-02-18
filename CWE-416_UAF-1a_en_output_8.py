
def create_buffer(buffer_size):
    buffer = bytearray(buffer_size)
    for i in range(buffer_size):
        buffer[i] = ord('A')
    return buffer
