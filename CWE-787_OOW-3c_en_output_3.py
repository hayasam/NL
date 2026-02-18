
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <argument>")
        sys.exit(1)
    
    # Get the argument and strip trailing whitespace
    argument = sys.argv[1].rstrip()
    
    print(argument)

if __name__ == "__main__":
    main()
