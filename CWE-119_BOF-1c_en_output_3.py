
def mem_copy(dest, src, num_bytes):
    for i in range(num_bytes):
        dest[i] = src[i]

def string_length(s):
    length = 0
    while s[length] != 0:
        length += 1
    return length

buffer = bytearray(10)
src_str = b"Hello\0"
mem_copy(buffer, src_str, string_length(src_str))
