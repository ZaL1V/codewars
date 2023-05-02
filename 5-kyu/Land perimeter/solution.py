def land_perimeter(arr):
    perimeter = 0
    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 'X':
                perimeter += 4
                if i > 0 and arr[i - 1][j] == 'X':
                    perimeter -= 2
                if j > 0 and arr[i][j - 1] == 'X':
                    perimeter -= 2

    return f"Total land perimeter: {perimeter}"
