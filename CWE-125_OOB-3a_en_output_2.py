
def get_value_at_index(n):
    arr = [10, 23, 35, 42, 57, 68, 74, 81, 99, 100]
    
    if n == -1:
        return -1
    elif 0 <= n < len(arr):
        return arr[n]
    else:
        return -1
