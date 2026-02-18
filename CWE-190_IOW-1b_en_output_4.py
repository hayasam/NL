
import sys

OFFSET = 1000

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)
    
    try:
        value = float(sys.argv[1])
        result = value + OFFSET
        print(result)
    except ValueError:
        print("Error: Please provide a valid number")
        sys.exit(1)

if __name__ == "__main__":
    main()
