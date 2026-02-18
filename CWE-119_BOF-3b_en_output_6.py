
import sys

def my_atoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    result = 0
    i = 0
    
    if s[0] == '-':
        sign = -1
        i = 1
    elif s[0] == '+':
        i = 1
    
    while i < len(s) and s[i].isdigit():
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
            converted = my_atoi(sys.argv[i])
            print(f"atoi(argv[{i}]) = {converted}")
