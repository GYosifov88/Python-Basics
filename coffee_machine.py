drink_type = input()
sugar_type = input()
number_of_drinks = int(input())
drink_price = 0
if drink_type == 'Espresso':
    if sugar_type == 'Without':
        drink_price = 0.90
    elif sugar_type == 'Normal':
        drink_price = 1
    elif sugar_type == 'Extra':
        drink_price = 1.20
elif drink_type == 'Cappuccino':
    if sugar_type == 'Without':
        drink_price = 1
    elif sugar_type == 'Normal':
        drink_price = 1.20
    elif sugar_type == 'Extra':
        drink_price = 1.60
elif drink_type == 'Tea':
    if sugar_type == 'Without':
        drink_price = 0.50
    elif sugar_type == 'Normal':
        drink_price = 0.60
    elif sugar_type == 'Extra':
        drink_price = 0.70

total_price = number_of_drinks * drink_price

if sugar_type == 'Without':
    total_price = total_price - (total_price * 0.35)
if drink_type == 'Espresso' and number_of_drinks >= 5:
    total_price = total_price - (total_price * 0.25)
if total_price > 15:
    total_price = total_price - (total_price * 0.20)

print(f'You bought {number_of_drinks} cups of {drink_type} for {total_price:.2f} lv.')
