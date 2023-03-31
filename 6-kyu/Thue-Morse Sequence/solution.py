def thue_morse(n):
    string = '01'
    string2 = ''
    while len(string) < n:
        for i in string:
            if i == '0':
                string2 += '1'
            else:
                string2 += '0'
        string += string2
        string2 = ''
    return string[0:n]
