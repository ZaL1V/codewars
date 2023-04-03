def first_non_repeating_letter(string):
    low_string = string.lower()
    for i in list(low_string):
        if low_string.count(i) == 1:
            num = list(low_string).index(i)
            return list(string)[num]
    return ''

#-------------improved version-------------#

def first_non_repeating_letter(string):

    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    return ''
