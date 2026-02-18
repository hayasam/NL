
def get_value_at_index(arr, index):
    if 0 <= index < len(arr):
        return arr[index]
    else:
        return -1

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    try:
        user_input = int(input("Enter an index: "))
        result = get_value_at_index(arr, user_input)
        print(result)
    except ValueError:
        print("Invalid input. Please enter an integer.")
