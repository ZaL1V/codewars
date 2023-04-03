def make_readable(s):
    return f'{s//3600:02d}:{(s%3600)//60:02d}:{s%60:02d}'
