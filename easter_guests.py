import math

number_of_guests = int(input())
budget = int(input())

number_of_sugar_breads = math.ceil(number_of_guests / 3)
number_of_eggs = number_of_guests * 2

eggs_cost = number_of_eggs * 0.45
sugar_bread_cost = number_of_sugar_breads * 4

total_cost = eggs_cost + sugar_bread_cost

difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Lyubo bought {number_of_sugar_breads} Easter bread and {number_of_eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")