
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <number>")
        return 1
    
    try:
        value = float(sys.argv[1])
        result = value + 1000
        print(result)
        return 0
    except ValueError:
        print("Error: Please provide a valid number")
        return 1

if __name__ == "__main__":
    sys.exit(main())
