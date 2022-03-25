budget = int(input())
season = input()
number_of_fishermen = int(input())
boat_price = 0
discount = 0
if season == 'Spring':
    if number_of_fishermen <= 6:
        boat_price = 3000 - (3000 * 10 / 100)
    elif 7 < number_of_fishermen <= 11:
        boat_price = 3000 - (3000 * 15 / 100)
    elif number_of_fishermen >= 12:
        boat_price = 3000 - (3000 * 25 / 100)
elif season == 'Summer' or season == 'Autumn':
    if number_of_fishermen <= 6:
        boat_price = 4200 - (4200 * 10 / 100)
    elif 7 < number_of_fishermen <= 11:
        boat_price = 4200 - (4200 * 15 / 100)
    elif number_of_fishermen >= 12:
        boat_price = 4200 - (4200 * 25 / 100)
elif season == 'Winter':
    if number_of_fishermen <= 6:
        boat_price = 2600 - (2600 * 10 / 100)
    elif 7 < number_of_fishermen <= 11:
        boat_price = 2600 - (2600 * 15 / 100)
    elif number_of_fishermen >= 12:
        boat_price = 2600 - (2600 * 25 / 100)

if number_of_fishermen % 2 == 0 and season != 'Autumn':
    boat_price = boat_price - boat_price * 5 / 100

difference = abs(budget - boat_price)

if budget >= boat_price:
    print(f'Yes! You have {difference:.2f} leva left.')
elif budget < boat_price:
    print(f'Not enough money! You need {difference:.2f} leva.')