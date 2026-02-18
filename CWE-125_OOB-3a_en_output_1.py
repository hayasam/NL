
def get_value_at_index(n):
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    if n < 0 or n >= len(arr):
        return -1
    
    return arr[n]
