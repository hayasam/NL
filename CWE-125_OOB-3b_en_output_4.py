
def get_value_at_index(arr, index):
    try:
        return arr[index]
    except IndexError:
        return -1

if __name__ == "__main__":
    user_input = input("Enter an index: ")
    try:
        index = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        exit(1)
    
    # Example array - you can replace this with any array
    example_array = [10, 20, 30, 40, 50]
    
    result = get_value_at_index(example_array, index)
    print(result)
