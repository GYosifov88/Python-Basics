fuel_type = input()
litres_of_fuel =  float(input())
discount_card = input()

if fuel_type == 'Gas':
    if discount_card == 'Yes':
        gas_price = 0.93 - 0.08
    else:
        gas_price = 0.93
elif fuel_type == 'Gasoline':
    if discount_card == 'Yes':
        gas_price = 2.22 - 0.18
    else:
        gas_price = 2.22
elif fuel_type == 'Diesel':
    if discount_card == 'Yes':
        gas_price = 2.33 - 0.12
    else:
        gas_price = 2.33

fuel_price = litres_of_fuel * gas_price

if 20 <= litres_of_fuel <= 25:
    fuel_price = fuel_price - (fuel_price * 0.08)
elif litres_of_fuel > 25:
    fuel_price = fuel_price - (fuel_price * 0.1)

print(f'{fuel_price:.2f} lv.')