
import sys

OFFSET = 1000

if len(sys.argv) > 1:
    try:
        value = float(sys.argv[1])
        result = value + OFFSET
        print(result)
    except ValueError:
        print("Error: Please provide a valid number")
else:
    print("Error: No value provided")
