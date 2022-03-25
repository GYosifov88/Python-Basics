number_of_visitors = int(input())
back_training = 0
chest_training = 0
legs_training = 0
abs_training = 0
shakes_bought = 0
bar_bought = 0
training_people = 0
non_training_people = 0
for i in range (number_of_visitors):
    fitness_visit = input()
    if fitness_visit == 'Back':
        back_training += 1
        training_people += 1
    elif fitness_visit == 'Chest':
        chest_training += 1
        training_people += 1
    elif fitness_visit == 'Legs':
        legs_training += 1
        training_people += 1
    elif fitness_visit == 'Abs':
        abs_training += 1
        training_people += 1
    elif fitness_visit == 'Protein shake':
        shakes_bought += 1
        non_training_people += 1
    elif fitness_visit == 'Protein bar':
        bar_bought += 1
        non_training_people += 1
percent_training = (training_people / number_of_visitors) * 100
percent_non_training = (non_training_people / number_of_visitors) * 100

print(f"{back_training} - back")
print(f"{chest_training} - chest")
print(f"{legs_training} - legs")
print(f"{abs_training} - abs")
print(f"{shakes_bought} - protein shake")
print(f"{bar_bought} - protein bar")
print(f"{percent_training:.2f}% - work out")
print(f"{percent_non_training:.2f}% - protein")
