
def copy_memory(destination, source, num_bytes):
    if num_bytes <= 0:
        return
    
    for i in range(num_bytes):
        if i >= 256:  # Buffer limit check
            break
        destination[i] = source[i]
