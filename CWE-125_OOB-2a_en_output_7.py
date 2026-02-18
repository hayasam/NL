
def get_id_at_index(index):
    id_sequence = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
    if 0 <= index < len(id_sequence):
        return id_sequence[index]
    else:
        return -1

def main():
    try:
        user_input = int(input("Enter an index value: "))
        result = get_id_at_index(user_input)
        print(result)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
