
def copy_memory(dest, src, num_bytes):
    if num_bytes <= 0:
        return
    
    for i in range(num_bytes):
        if i >= 256:
            break
        dest[i] = src[i]
