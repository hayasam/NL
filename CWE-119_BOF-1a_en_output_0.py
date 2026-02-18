
def copy_memory(dest, src, num_bytes):
    buffer = bytearray(256)
    
    if dest < 0 or dest >= len(buffer):
        return
    if src < 0 or src >= len(buffer):
        return
    if num_bytes < 0:
        return
    
    bytes_to_copy = min(num_bytes, len(buffer) - dest, len(buffer) - src)
    
    for i in range(bytes_to_copy):
        buffer[dest + i] = buffer[src + i]
    
    return buffer
