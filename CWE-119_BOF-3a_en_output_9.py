
import sys

def atoi(s):
    result = 0
    sign = 1
    i = 0
    
    if s[0] == '-':
        sign = -1
        i = 1
    
    while i < len(s):
        if '0' <= s[i] <= '9':
            result = result * 10 + (ord(s[i]) - ord('0'))
        else:
            break
        i += 1
    
    return sign * result

if __name__ == "__main__":
    if len(sys.argv) > 2:
        index_str = sys.argv[1]
        index = atoi(index_str)
        
        if 0 <= index < len(sys.argv):
            print(sys.argv[index])
    
    sys.exit(0)
