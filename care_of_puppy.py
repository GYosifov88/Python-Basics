total_food = int(input())
total_food_grams = total_food * 1000
is_food_over = False

command = input()

while command != 'Adopted':
    eaten_food = int(command)
    total_food_grams -= eaten_food
    if total_food_grams < 0:
        is_food_over = True


    command = input()

if is_food_over:
    print(f'Food is not enough. You need {abs(total_food_grams)} grams more.')
else:
    print(f'Food is enough! Leftovers: {abs(total_food_grams)} grams.')