import sys

number_painted_eggs = int(input())
max_painted_eggs = -sys.maxsize
max_color = ''
number_of_red_eggs = 0
number_of_orange_eggs = 0
number_of_blue_eggs = 0
number_of_green_eggs = 0
for eggs in range (number_painted_eggs):
    egg_color = input()

    if egg_color == 'red':
        number_of_red_eggs += 1
        if number_of_red_eggs > max_painted_eggs:
            max_painted_eggs = number_of_red_eggs
            max_color = 'red'
    elif egg_color == 'orange':
        number_of_orange_eggs += 1
        if number_of_orange_eggs > max_painted_eggs:
            max_painted_eggs = number_of_orange_eggs
            max_color = 'orange'
    elif egg_color == 'blue':
        number_of_blue_eggs += 1
        if number_of_blue_eggs > max_painted_eggs:
            max_painted_eggs = number_of_blue_eggs
            max_color = 'blue'
    elif egg_color == 'green':
        number_of_green_eggs += 1
        if number_of_green_eggs > max_painted_eggs:
            max_painted_eggs = number_of_green_eggs
            max_color = 'green'

print(f"Red eggs: {number_of_red_eggs}")
print(f"Orange eggs: {number_of_orange_eggs}")
print(f"Blue eggs: {number_of_blue_eggs}")
print(f"Green eggs: {number_of_green_eggs}")
print(f"Max eggs: {max_painted_eggs} -> {max_color}")
