
def memcpy(dest, src, n):
    for i in range(n):
        dest[i] = src[i]

def strlen(s):
    length = 0
    while s[length] != 0:
        length += 1
    return length

# Copy "Hello" to buffer
source = "Hello"
buffer = [0] * 100  # Destination buffer

# Convert source to list of ASCII values with null terminator
src_bytes = [ord(c) for c in source] + [0]
memcpy(buffer, src_bytes, len(src_bytes))
