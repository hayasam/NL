
def mem_copy(dest, src, num_bytes):
    for i in range(num_bytes):
        dest[i] = src[i]

def string_length(s):
    length = 0
    for char in s:
        length += 1
    return length

message = "Hello, World!"
buffer = bytearray(100)

msg_bytes = message.encode('utf-8')
mem_copy(buffer, msg_bytes, string_length(msg_bytes))
