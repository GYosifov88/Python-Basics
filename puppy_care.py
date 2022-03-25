kilos_of_bought_dog_food = int(input())

grams_of_bought_dog_food = kilos_of_bought_dog_food * 1000
total_eaten_food = 0
command = input()
while command != 'Adopted':
    eaten_food_per_day = int(command)
    total_eaten_food += eaten_food_per_day

    command = input()
difference = abs(total_eaten_food - grams_of_bought_dog_food)
if grams_of_bought_dog_food >= total_eaten_food:
    print (f"Food is enough! Leftovers: {difference} grams.")
else:
    print (f"Food is not enough. You need {difference} grams more." )
