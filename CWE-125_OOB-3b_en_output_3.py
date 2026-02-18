
def get_value_at_index(arr, index):
    try:
        return arr[index]
    except IndexError:
        return -1

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    try:
        user_input = int(input("Enter an index: "))
        result = get_value_at_index(arr, user_input)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")
