def rotate(s):
    result = []
    for i in s:
        s = s[1:] + s[0]
        result.append(s)
    return result

#-------------improved version-------------#

def rotate(s):
    return [s[i+1:] + s[:i+1] for i in range(len(s))]
