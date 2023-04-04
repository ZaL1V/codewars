def tower_builder(n):
    tower = []
    floor = ''

    for i in range(n):
        stars = '*' * (i * 2 + 1)
        spaces = ' ' * (n - i - 1)
        floor = spaces + stars + spaces
        tower.append(floor)

    return tower
