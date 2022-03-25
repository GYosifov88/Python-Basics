fuel_type = input()
litres_of_fuel = int(input())

if fuel_type == 'Diesel':
    if litres_of_fuel >=25:
        print(f'You have enough {str.lower(fuel_type)}.')
    elif litres_of_fuel < 25:
        print(f'Fill your tank with {str.lower(fuel_type)}!')
elif fuel_type == 'Gasoline':
    if litres_of_fuel >=25:
        print(f'You have enough {str.lower(fuel_type)}.')
    elif litres_of_fuel < 25:
        print(f'Fill your tank with {str.lower(fuel_type)}!')
elif fuel_type == 'Gas':
    if litres_of_fuel >=25:
        print(f'You have enough {str.lower(fuel_type)}.')
    elif litres_of_fuel < 25:
        print(f'Fill your tank with {str.lower(fuel_type)}!')
else:
    print('Invalid fuel!')