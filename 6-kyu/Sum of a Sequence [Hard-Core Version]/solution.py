def sequence_sum(begin_number, end_number, step):
    num = (end_number - begin_number) // step + 1
    return (2 * begin_number + step * (num - 1)) * num // 2 if num >= 0 else 0
