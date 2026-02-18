
import sys

def scan(format_string):
    if format_string != "%s\n":
        return -1
    
    buffer = sys.stdin.readline()
    
    if not buffer:
        return -1
    
    if buffer.endswith('\n'):
        buffer = buffer[:-1]
    
    if len(buffer) > 1023:
        buffer = buffer[:1023]
    
    return len(buffer)

def scanf(format_string, buffer):
    if format_string != "%s":
        return -1
    
    result = scan("%s\n")
    
    if result == -1:
        return -1
    
    temp_buffer = sys.stdin.readline()
    if not temp_buffer:
        return -1
    
    if temp_buffer.endswith('\n'):
        temp_buffer = temp_buffer[:-1]
    
    if len(temp_buffer) > 1023:
        temp_buffer = temp_buffer[:1023]
    
    buffer.clear()
    buffer.extend(temp_buffer)
    
    return len(buffer)

if __name__ == "__main__":
    buf = bytearray(1024)
    result = scanf("%s", buf)
    print(f"Read {result} characters: {buf.decode('utf-8', errors='ignore').rstrip(chr(0))}")
