import math
number_of_people = int(input())
entry_fee = float(input())
chair_price = float(input())
umbrella_price = float(input())

entry_cost = number_of_people * entry_fee
number_of_umbrella = math.ceil(number_of_people / 2)
number_of_chairs = math.ceil(number_of_people * 0.75)
umbrella_cost = number_of_umbrella * umbrella_price
chair_cost = number_of_chairs * chair_price
total_cost = entry_cost + umbrella_cost + chair_cost

print (f'{total_cost:.2f} lv.')