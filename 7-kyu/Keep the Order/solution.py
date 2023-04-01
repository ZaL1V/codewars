def keep_order(arr, val):
    for i, value in enumerate(arr):
        if value >= val:
            return i
    return len(arr)
