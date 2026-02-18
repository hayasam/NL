
import sys

def getValueFromArray(array, size, index):
    if 0 <= index < size:
        return array[index]
    else:
        return -1

def main():
    id_sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    size = len(id_sequence)
    
    try:
        index = int(sys.stdin.readline().strip())
    except ValueError:
        index = -1
    
    result = getValueFromArray(id_sequence, size, index)
    sys.exit(result)

if __name__ == "__main__":
    main()
