def longest_repetition(chars):
    letter = ''
    count = 0
    counter = 1
    test_letter = ''
    for l in chars:
        if l == test_letter:
            counter += 1
        else:
            test_letter = l
            counter = 1
        if counter > count:
            count = counter
            letter = test_letter

    return letter, count
