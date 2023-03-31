def convert_palindromes(numbers):
    for i, number in enumerate(numbers):
            numbers[i] = 1  if str(number) == str(number)[::-1] else 0
    return numbers

#-----------------------------------------------#
def convert_palindromes(numbers):
    for i, number in enumerate(numbers):
        if str(number) == str(number)[::-1]:
            numbers[i] = 1
        else:
            numbers[i] = 0
    return numbers
