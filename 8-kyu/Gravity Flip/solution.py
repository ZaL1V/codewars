def flip(d, a):
    state = False if d == 'R' else True
    a.sort(reverse=state)
    return a
