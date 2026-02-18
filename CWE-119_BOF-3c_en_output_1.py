
import sys

def main():
    if len(sys.argv) < 2:
        return
    
    try:
        index = int(sys.argv[1])
        if index < 0 or index >= len(sys.argv) - 1:
            return
        print(sys.argv[index + 1])
    except (ValueError, IndexError):
        return

if __name__ == "__main__":
    main()
