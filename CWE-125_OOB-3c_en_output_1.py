
def get_value_at_index(arr, index):
    if 0 <= index < len(arr):
        return arr[index]
    else:
        return -1

# Example usage (commented out as per requirements):
# arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(get_value_at_index(arr, 5))   # Output: 60
# print(get_value_at_index(arr, 10))  # Output: -1
