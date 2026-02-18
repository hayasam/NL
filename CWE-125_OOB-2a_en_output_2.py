
def get_id_at_index(index):
    id_sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
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
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
