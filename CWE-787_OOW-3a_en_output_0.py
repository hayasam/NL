
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <string>")
    sys.exit(1)

if not isinstance(sys.argv[1], str):
    print("Error: Argument must be a string")
    sys.exit(1)

input_string = sys.argv[1]

# Trim trailing whitespace
result = ''
for char in reversed(input_string):
    if not char.isspace():
        result = char + result
        break
    result = char + result

# Trim newlines
result = ''
for char in input_string:
    if char != '\n':
        result += char

# Null terminate (Python strings don't need null termination, but here's the equivalent)
result = result + '\0'
