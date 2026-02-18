
import sys

if len(sys.argv) != 2:
    sys.exit(1)

if not isinstance(sys.argv[1], str):
    sys.exit(1)

result = sys.argv[1]

while result.endswith(' ') or result.endswith('\t'):
    result = result[:-1]

while result.endswith('\n') or result.endswith('\r'):
    result = result[:-1]

result = result + '\0'
