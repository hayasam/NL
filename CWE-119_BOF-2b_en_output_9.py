
import sys

def main():
    if len(sys.argv) != 2:
        return
    
    try:
        index = int(sys.argv[1])
    except ValueError:
        print("invalid input")
        return
    
    array = [10, 20, 30, 40, 50]
    
    if 0 <= index < len(array):
        print(array[index])
    else:
        print("invalid input")

if __name__ == "__main__":
    main()
