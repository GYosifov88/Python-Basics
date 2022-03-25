number_of_days = int(input())
total_food = float(input())
bisquits = 0
total_bisquits = 0
total_food_eaten = 0
total_dog_eaten = 0
total_cat_eaten = 0
for i in range (1, number_of_days + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_dog_eaten += dog_food
    total_cat_eaten += cat_food
    if i % 3 == 0:
        bisquits = (cat_food + dog_food) * 10 / 100
        total_bisquits += bisquits

total_food_eaten = total_cat_eaten + total_dog_eaten
total_food_eaten_percent = total_food_eaten / total_food * 100
dog_percent = total_dog_eaten / total_food_eaten * 100
cat_percent = total_cat_eaten / total_food_eaten * 100

print (f'Total eaten biscuits: {round(total_bisquits)}gr.')
print (f'{total_food_eaten_percent:.2f}% of the food has been eaten.')
print (f'{dog_percent:.2f}% eaten from the dog.')
/.,print (f'{cat_percent:.2f}% eaten from the cat.')

