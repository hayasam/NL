
def copy_memory(dest, src, num_bytes):
    if num_bytes <= 0:
        return
    
    buffer_size = 256
    bytes_to_copy = min(num_bytes, buffer_size)
    
    for i in range(bytes_to_copy):
        dest[i] = src[i]
