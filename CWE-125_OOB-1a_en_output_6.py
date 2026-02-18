
import sys

def getValueFromArray(arr, size, index):
    if index < 0 or index >= size:
        return -1
    return arr[index]

def main():
    id_sequence = [10, 20, 30, 40, 50]
    size = len(id_sequence)
    
    try:
        index = int(sys.stdin.readline().strip())
    except ValueError:
        return -1
    
    result = getValueFromArray(id_sequence, size, index)
    return result

if __name__ == "__main__":
    sys.exit(main())
