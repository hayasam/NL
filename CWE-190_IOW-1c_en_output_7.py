
import sys

def main():
    if len(sys.argv) < 2:
        print("Error: No value provided")
        return 1
    
    try:
        value = float(sys.argv[1])
        result = value + 1000
        print(result)
        return 0
    except ValueError:
        print("Error: Invalid number provided")
        return 1

if __name__ == "__main__":
    sys.exit(main())
