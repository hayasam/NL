
import sys

def main():
    if len(sys.argv) < 2:
        return
    
    try:
        index = int(sys.argv[1])
        if index < 0:
            return
        
        target_index = index + 1
        if target_index < len(sys.argv):
            print(sys.argv[target_index])
    except ValueError:
        return

if __name__ == "__main__":
    main()
