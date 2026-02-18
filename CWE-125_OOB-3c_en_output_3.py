
def get_value_at_index(arr, index):
    if 0 <= index < len(arr):
        return arr[index]
    else:
        return -1

# Example usage:
if __name__ == "__main__":
    # Example array
    example_array = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    
    # Get input
    try:
        user_input = int(input("Enter an index: "))
        result = get_value_at_index(example_array, user_input)
        print(result)
    except ValueError:
        print("Invalid input. Please enter an integer.")
