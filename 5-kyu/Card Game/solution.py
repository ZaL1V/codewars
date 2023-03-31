from decimal import Decimal

def card_game(n):
    n = Decimal(n)
    alice = 0
    while n != 0:
        for i in range(2):
            selection = 1 if (n / 2) % 2 == 0 and n > 4 or n % 2 != 0 else n // 2
            alice = alice + selection if i == 0 else alice
            n -= selection
    return alice
