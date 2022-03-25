number_of_cats = int(input())
small_group = 0
medium_group = 0
large_group = 0
total_eaten_food = 0
for cat in range (number_of_cats):
    eaten_food = float(input())
    total_eaten_food += eaten_food
    if 100 <= eaten_food < 200:
        small_group += 1
    elif 200 <= eaten_food < 300:
        medium_group += 1
    elif 300 <= eaten_food < 400:
        large_group += 1

food_cost = total_eaten_food * 0.01245

print(f"Group 1: {small_group} cats.")
print(f"Group 2: {medium_group} cats.")
print(f"Group 3: {large_group} cats.")
print(f"Price for food per day: {food_cost:.2f} lv.")
