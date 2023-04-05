def add_length(str):
    separator = str.split(' ')
    return [f"{i} {len(i)}" for i in separator]
