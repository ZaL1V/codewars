def sort_emotions(arr, order):
    item2 = {1:':D', 2:':)', 3:':|', 4:':(', 5:'T_T'}
    item1 = {':D':1, ':)':2, ':|':3, ':(':4, 'T_T':5}
    sort_id = [item1[i] for i in arr]
    sort_id.sort(reverse = not order)
    sort_by_id = [item2[i] for i in sort_id]
    return sort_by_id
