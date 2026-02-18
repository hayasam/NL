
def get_value_at_index(index):
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    if index < 0 or index >= len(arr):
        return -1
    
    return arr[index]
