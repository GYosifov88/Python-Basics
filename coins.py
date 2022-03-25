sum = float(input())
sum = int(sum * 100)
number_of_coins = 0
number_of_coins += sum // 200
sum %= 200
number_of_coins += sum // 100
sum %= 100
number_of_coins += sum // 50
sum %= 50
number_of_coins += sum // 20
sum %= 20
number_of_coins += sum // 10
sum %= 10
number_of_coins += sum // 5
sum %= 5
number_of_coins += sum // 2
sum %= 2
number_of_coins += sum // 1
sum %= 1

print(f'{number_of_coins}')