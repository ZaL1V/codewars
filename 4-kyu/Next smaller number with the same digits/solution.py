def next_smaller(n):
    digits = list(str(n))
    i = len(digits) - 1
    while i > 0 and digits[i] >= digits[i - 1]:
        i -= 1
        
    if i == 0:
        return -1
    digits_num = i
    
    while digits_num < len(digits) and digits[digits_num] < digits[i - 1]:
        digits_num += 1
        
    digits[i-1], digits[digits_num-1] = digits[digits_num-1], digits[i-1]
    digits[i:] = sorted(digits[i:], reverse=True)
    result = int(''.join(digits))
    
    if len(str(result)) != len(str(n)):
        return -1

    return result