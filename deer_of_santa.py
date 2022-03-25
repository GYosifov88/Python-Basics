import math

number_of_days = int(input())
left_food_kg = int(input())
food_per_day_first_deer_kg = float(input())
food_per_day_second_deer_kg = float(input())
food_per_day_third_deer_kg = float(input())


total_eaten_food_first_deer = number_of_days * food_per_day_first_deer_kg
total_eaten_food_second_deer = number_of_days * food_per_day_second_deer_kg
total_eaten_food_third_deer = number_of_days * food_per_day_third_deer_kg

total_food_eaten = total_eaten_food_first_deer + total_eaten_food_second_deer + total_eaten_food_third_deer

difference = abs(left_food_kg - total_food_eaten)

if left_food_kg >= total_food_eaten:
    print (f'{math.floor(difference)} kilos of food left.')
else:
    print (f'{math.ceil(difference)} more kilos of food are needed.')