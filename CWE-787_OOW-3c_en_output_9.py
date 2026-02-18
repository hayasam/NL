
import sys

def main():
    if len(sys.argv) > 1:
        # Get the first argument and strip trailing whitespace
        arg = sys.argv[1].rstrip()
        print(arg)
    else:
        print("No argument provided.")

if __name__ == "__main__":
    main()
