
import sys

def atoi(s):
    result = 0
    sign = 1
    i = 0
    
    if len(s) == 0:
        return 0
    
    # Handle sign
    if s[0] == '-':
        sign = -1
        i = 1
    elif s[0] == '+':
        i = 1
    
    # Convert characters to integer
    while i < len(s):
        if '0' <= s[i] <= '9':
            result = result * 10 + (ord(s[i]) - ord('0'))
            i += 1
        else:
            break
    
    return sign * result

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    
    index = atoi(sys.argv[1])
    
    if 0 <= index < len(sys.argv):
        print(sys.argv[index])
    
    sys.exit(0)
