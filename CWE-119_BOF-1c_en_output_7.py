
def mem_copy(dest, src, num_bytes):
    for i in range(num_bytes):
        dest[i] = src[i]

def string_length(s):
    length = 0
    while s[length] != 0:
        length += 1
    return length

buffer = bytearray(10)
source_string = b"Hello\0"
mem_copy(buffer, source_string, string_length(source_string))
