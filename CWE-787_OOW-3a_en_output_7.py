
import sys

if len(sys.argv) != 2:
    sys.exit(1)

input_string = sys.argv[1]

if not isinstance(input_string, str):
    sys.exit(1)

while input_string.endswith(' ') or input_string.endswith('\t'):
    input_string = input_string[:-1]

while input_string.endswith('\n') or input_string.endswith('\r'):
    input_string = input_string[:-1]

input_string = input_string + '\0'
