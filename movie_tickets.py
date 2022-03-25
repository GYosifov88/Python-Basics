number_a1 = int(input())
number_a2 = int(input())
number_n = int(input())
interval = int(number_n / 2)
sum = 0
for symbol1 in range (number_a1, number_a2):
    first_symbol = chr(symbol1)
    for symbol2 in range (1, number_n):
        second_symbol = symbol2
        for symbol3 in range (1, interval):
            third_symbol = symbol3
            fourth_symbol = ord(first_symbol)
            sum = fourth_symbol + second_symbol+ third_symbol
            if ord(first_symbol) % 2 != 0 and sum % 2 !=0:
                print(f'{first_symbol}-{second_symbol}{third_symbol}{fourth_symbol}')

