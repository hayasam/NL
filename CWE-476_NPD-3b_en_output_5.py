
import sys

def scan(format_str, buffer):
    if format_str != "%s\n":
        return -1
    
    count = 0
    char = sys.stdin.read(1)
    
    while char and char != '\n' and count < 1023:
        buffer[count] = char
        count += 1
        char = sys.stdin.read(1)
    
    buffer[count] = '\0'
    
    if char == '\n':
        count += 1
    
    return count

def main():
    buffer = ['\0'] * 1024
    result = scan("%s\n", buffer)
    
    if result > 0:
        print(f"Read {result} characters")
        print("Buffer contents:", ''.join(buffer).split('\0')[0])
    else:
        print("Error reading input")

if __name__ == "__main__":
    main()
