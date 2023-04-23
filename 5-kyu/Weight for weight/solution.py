def order_weight(strng):
    numbers = strng.split()
    numbers.sort(key=lambda num: (sum(int(digit) for digit in num), num))
    return ' '.join(numbers)
