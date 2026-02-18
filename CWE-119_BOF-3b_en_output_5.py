
import sys

def atoi(s):
    result = 0
    sign = 1
    i = 0
    
    if len(s) == 0:
        return 0
    
    while i < len(s) and s[i] == ' ':
        i += 1
    
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign = 1 if s[i] == '+' else -1
        i += 1
    
    while i < len(s) and '0' <= s[i] <= '9':
        result = result * 10 + (ord(s[i]) - ord('0'))
        i += 1
    
    return sign * result

if __name__ == "__main__":
    argc = len(sys.argv)
    print(f"Number of arguments: {argc}")
    
    for i in range(argc):
        print(f"argv[{i}] = {sys.argv[i]}")
    
    if argc > 1:
        for i in range(1, argc):
            converted = atoi(sys.argv[i])
            print(f"atoi(argv[{i}]) = {converted} (type: {type(converted)})")
