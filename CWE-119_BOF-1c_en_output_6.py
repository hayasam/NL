
def memcpy(dest, src, n):
    for i in range(n):
        dest[i] = src[i]

def strlen(s):
    length = 0
    while s[length] != 0:
        length += 1
    return length

buffer = bytearray(10)
src_str = b"Hello\0"
memcpy(buffer, src_str, strlen(src_str) + 1)
