
import sys

def getValueFromArray(array, size, index):
    if index < 0 or index >= size:
        return -1
    return array[index]

def main():
    id_sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    size = len(id_sequence)
    
    try:
        index = int(sys.stdin.readline().strip())
    except ValueError:
        return -1
    
    return getValueFromArray(id_sequence, size, index)

if __name__ == "__main__":
    sys.exit(main())
