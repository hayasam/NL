
def get_id_sequence_value():
    id_sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    try:
        index = int(input("Enter an index value: "))
    except ValueError:
        return 0
    
    if 0 <= index < len(id_sequence):
        return id_sequence[index]
    else:
        return 0
