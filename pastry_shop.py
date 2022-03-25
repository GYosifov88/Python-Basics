pastry_kind = input()
number_pastries = int(input())
day_of_december_before_christmas = int(input())
cost = 0
if pastry_kind == 'Cake':
    if day_of_december_before_christmas <= 15:
        price = 24
    elif day_of_december_before_christmas > 15:
        price = 28.70
elif pastry_kind == 'Souffle':
    if day_of_december_before_christmas <= 15:
        price = 6.66
    elif day_of_december_before_christmas > 15:
        price = 9.80
elif pastry_kind == 'Baklava':
    if day_of_december_before_christmas <= 15:
        price = 12.60
    elif day_of_december_before_christmas > 15:
        price = 16.98

cost = price * number_pastries

if day_of_december_before_christmas <= 22:
    if 100 <= cost <= 200:
        cost = cost - (cost * 15 / 100)
    elif cost > 200:
        cost = cost - (cost * 25 / 100)

if day_of_december_before_christmas <= 15:
    cost = cost - (cost * 10 / 100)

print(f'{cost:.2f}')