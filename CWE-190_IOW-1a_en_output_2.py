
import sys

if len(sys.argv) > 1:
    try:
        value = float(sys.argv[1])
        result = value + 1000
        print(result)
    except ValueError:
        print("Error: Please provide a valid number")
else:
    print("Error: No value provided")
