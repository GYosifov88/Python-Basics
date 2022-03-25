import math

number_of_days = int(input())
left_food_kg = int(input())
food_for_dog_kg = float(input())
food_for_cat_kg = float(input())
food_for_turtle_grams = float(input())

food_for_turtle_kg = food_for_turtle_grams / 1000

food_per_day_left = left_food_kg / number_of_days

total_dog_to_eat = number_of_days * food_for_dog_kg
total_cat_to_eat = number_of_days * food_for_cat_kg
total_turtle_to_eat = number_of_days * food_for_turtle_kg

total_to_eat = total_turtle_to_eat + total_cat_to_eat + total_dog_to_eat

difference = abs(left_food_kg - total_to_eat)

if left_food_kg >= total_to_eat:
    print (f'{math.floor(difference)} kilos of food left.')
else:
    print (f'{math.ceil(difference)} more kilos of food are needed.')