
def get_id_sequence_value():
    id_sequence = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
    
    try:
        index = int(input("Enter an index value: "))
    except ValueError:
        return 0
    
    if 0 <= index < len(id_sequence):
        return id_sequence[index]
    else:
        return 0
