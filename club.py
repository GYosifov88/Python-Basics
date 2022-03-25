wanted_profit = float(input())
is_wanted_profit_gained = False
total_amount = 0
cocktail = input()

while cocktail != 'Party!':
    number_of_cocktails = int(input())
    cocktail_price = len(cocktail)
    order_price = cocktail_price * number_of_cocktails

    if order_price % 2 != 0:
       order_price = order_price - order_price * 0.25
    total_amount += order_price
    if total_amount >= wanted_profit:
        is_wanted_profit_gained = True
        break

    cocktail = input()

difference = abs(wanted_profit - total_amount)
if is_wanted_profit_gained:
    print ('Target acquired.')
    print (f'Club income - {total_amount:.2f} leva.')
else:
    print (f'We need {difference:.2f} leva more.')
    print (f'Club income - {total_amount:.2f} leva.')