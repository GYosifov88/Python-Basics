number_of_bottles_of_detergent = int(input())
number_of_plates = 0
number_of_pots = 0
ml_of_detergent = 750 * number_of_bottles_of_detergent
needed_detergent = 0
left_detergent = 0
detergent_not_enough = False
counter = 0
command = input()
while command != 'End':
    number_of_dishes = int(command)
    counter += 1

    if counter % 3 == 0:
        number_of_pots += number_of_dishes
        needed_detergent = number_of_dishes * 15
        ml_of_detergent -= needed_detergent
        left_detergent = ml_of_detergent


    else:
        number_of_plates += number_of_dishes
        needed_detergent = number_of_dishes * 5
        ml_of_detergent -= needed_detergent
        left_detergent = ml_of_detergent

    difference = abs(left_detergent)

    if left_detergent < 0:
        detergent_not_enough = True
        print(f"Not enough detergent, {difference} ml. more necessary!")
        break



    command = input()



difference = abs(left_detergent)

if not detergent_not_enough:
    print("Detergent was enough!")
    print(f"{number_of_plates} dishes and {number_of_pots} pots were washed.")
    print(f"Leftover detergent {difference} ml.")



