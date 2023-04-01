def land_perimeter(arr):
    perimeter = 0
    storage = ''
    box1 = ''
    box2 = ''
    for item in arr:
        box1 = [i for i, c in enumerate(item) if c == 'X']
        for bx1 in box1:
            for bx2 in box2:
                if bx1 == bx2:
                    perimeter -= 2
        box2 = [i for i, c in enumerate(item) if c == 'X']
        for i in item:
            if i == 'X':
                if i == storage:
                    perimeter -= 2
                perimeter += 4
            storage = i
        storage = ''
    return f"Total land perimeter: {perimeter}"
