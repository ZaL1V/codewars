def sum_of_intervals(intervals):
    intervals.sort()
    length = 0
    start, end = intervals[0]
    for interval in intervals[1:]:
        if interval[0] <= end:
            if interval[1] > end:
                end = interval[1]
        else:
            length += end - start
            start, end = interval
    length += end - start
    return length
