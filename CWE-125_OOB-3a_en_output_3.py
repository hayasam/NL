
def get_value_at_index(n):
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    if n == -1:
        return -1
    elif 0 <= n < len(arr):
        return arr[n]
    else:
        return -1
