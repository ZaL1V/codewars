def find_uniq(arr):
    unique = set(arr)
    for i in unique:
        if arr.count(i) == 1:
            return i

#-------------improved version-------------#

def find_uniq(arr):
    return [i for i in set(arr) if arr.count(i) == 1][0]
