def tower_builder(n, block_size):
    w, h = block_size
    tower = []
    floor = ''
    for i in range(n):
        stars = '*' *(i * 2 + 1) * w
        spaces = ' ' *(n - i - 1) * w
        floor = spaces + stars + spaces
        for i in range(h):
            tower.append(floor)
    return tower
