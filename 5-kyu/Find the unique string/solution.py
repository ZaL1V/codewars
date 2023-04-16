def find_uniq(arr):
    arr_list = []
    for i in arr:
        arr_list.append(set(i.lower()))
    unique = [i for i in arr_list if arr_list.count(i) == 1][0]
    result = arr_list.index(unique)
    return arr[result]

#-------------improved version-------------#

def find_uniq(arr):
    arr_list = [set(i.lower()) for i in arr]
    unique = [i for i in arr_list if arr_list.count(i) == 1][0]
    return arr[arr_list.index(unique)]
