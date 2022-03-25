starting_number_of_eggs = int(input())
current_number_of_eggs = starting_number_of_eggs
number_of_sold_egss = 0
number_of_added_eggs = 0
while True:
    command = input()
    if command == 'Close':
        print("Store is closed!")
        print(f"{number_of_sold_egss} eggs sold.")
        break
    number_of_eggs = int(input())

    if command == 'Buy' and number_of_eggs <= current_number_of_eggs:
        number_of_sold_egss += number_of_eggs
        current_number_of_eggs -= number_of_eggs
    elif command == 'Buy' and number_of_eggs > current_number_of_eggs:
        print("Not enough eggs in store!")
        print(f"You can buy only {current_number_of_eggs}.")
        break
    if command == 'Fill':
        number_of_added_eggs += number_of_eggs
        current_number_of_eggs += number_of_eggs

