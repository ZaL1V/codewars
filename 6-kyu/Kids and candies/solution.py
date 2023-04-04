def candies_to_buy(kids):
    num = 1
    for i in range(kids):
        box = num
        while num % (i+1):
            num += box
    return num
