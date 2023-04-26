def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

#-------------improved version-------------#

def find_it(seq):
    return [seq[i] for i in range(len(seq)) if seq.count(seq[i]) % 2 != 0][0]
