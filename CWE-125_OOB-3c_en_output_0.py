
def get_value_at_index(index):
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    if index < 0 or index >= len(arr):
        return -1
    return arr[index]

if __name__ == "__main__":
    try:
        user_input = int(input().strip())
        result = get_value_at_index(user_input)
        print(result)
    except ValueError:
        print(-1)
