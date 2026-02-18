
def memcpy(dest, src, num_bytes):
    for i in range(num_bytes):
        dest[i] = src[i]

def strlen(string):
    length = 0
    while string[length] != 0:
        length += 1
    return length

# Copy "Hello" to buffer
source_string = "Hello\0"
buffer = bytearray(256)
memcpy(buffer, source_string.encode('ascii'), strlen(source_string.encode('ascii')) + 1)
