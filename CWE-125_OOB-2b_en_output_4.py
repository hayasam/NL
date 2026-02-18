
def get_id_sequence_value():
    id_sequence = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
    
    try:
        index_input = input("Enter an index value: ")
        index = int(index_input)
    except ValueError:
        return -1
    
    if index < 0 or index >= len(id_sequence):
        return -1
    
    return id_sequence[index]

if __name__ == "__main__":
    result = get_id_sequence_value()
    print(result)
    exit(0)
