def next_bigger(n):
    num_list = [int(i) for i in str(n)]
    pos = len(num_list) - 1
    while pos > 0 and num_list[pos - 1] >= num_list[pos]:
        pos -= 1
    if pos == 0:
        return -1
    pivot = pos - 1
    pos = len(num_list) - 1
    while num_list[pos] <= num_list[pivot]:
        pos -= 1
    num_list[pivot], num_list[pos] = num_list[pos], num_list[pivot]
    num_list[pivot+1:] = reversed(num_list[pivot+1:])
    return int(''.join(map(str, num_list)))
