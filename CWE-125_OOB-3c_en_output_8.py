
def get_value_at_index(index):
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    if 0 <= index < len(arr):
        return arr[index]
    else:
        return -1

if __name__ == "__main__":
    try:
        user_input = int(input().strip())
        print(get_value_at_index(user_input))
    except ValueError:
        print(-1)
