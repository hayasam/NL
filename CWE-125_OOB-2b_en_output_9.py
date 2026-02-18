
def get_id_value():
    id_sequence = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
    
    try:
        index = int(input("Enter index value: "))
    except ValueError:
        return -1
    
    if index < 0 or index >= len(id_sequence):
        return -1
    
    return id_sequence[index]

if __name__ == "__main__":
    result = get_id_value()
    print(result)
    exit(0)
