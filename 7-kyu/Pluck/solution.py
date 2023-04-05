def pluck(objs, name):
    return [i[name] if name in i else None for i in objs]
