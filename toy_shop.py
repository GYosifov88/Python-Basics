price_excursion = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

price_puzzles = 2.60
price_dolls = 3
price_bears = 4.10
price_minions = 8.20
price_trucks = 2

total_price = (number_puzzles * price_puzzles) + (number_dolls * price_dolls) + (number_bears * price_bears) + (number_minions * price_minions) + (number_trucks * price_trucks)
total_number = number_trucks + number_bears + number_dolls + number_minions + number_puzzles

if total_number >= 50:
    total_price = total_price - total_price * 25 / 100

loan = total_price * 10 / 100

profit = total_price - loan

leftover = abs(profit - price_excursion)

if leftover > price_excursion:
    print(f'Yes! {leftover:.2f} lv left.')
else:
    print (f'Not enough money! {leftover:.2f} lv needed.')