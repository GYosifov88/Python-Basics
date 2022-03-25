import math
football_fan_name = input()
budget = float(input())
number_of_beers = int(input())
number_of_chips = int(input())

beer_cost = number_of_beers * 1.20
price_of_chips = beer_cost * 45 / 100
chips_cost = math.ceil(number_of_chips * price_of_chips)

total_cost = chips_cost + beer_cost

difference = abs(total_cost - budget)

if budget >= total_cost:
    print (f"{football_fan_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{football_fan_name} needs {difference:.2f} more leva!")