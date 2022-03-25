import math

tenis_rocket_price = float(input())
number_of_tenis_rockets = int(input())
number_of_sketchers = int(input())

sketchers_price = tenis_rocket_price / 6
tenis_rocket_cost = tenis_rocket_price * number_of_tenis_rockets
sketchers_cost = number_of_sketchers * sketchers_price
full_cost = tenis_rocket_cost + sketchers_cost
other_equipment = full_cost * 0.2

total_cost = full_cost + other_equipment

djokovich_cost = total_cost / 8
sponsors_cost = total_cost - djokovich_cost

print(f"Price to be paid by Djokovic {math.floor(djokovich_cost)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_cost)}")
