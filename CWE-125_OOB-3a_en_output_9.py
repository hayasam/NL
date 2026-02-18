
def get_value_at_index(index):
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    if index == -1:
        return -1
    elif 0 <= index < len(arr):
        return arr[index]
    else:
        return -1
