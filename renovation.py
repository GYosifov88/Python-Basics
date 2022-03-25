import math

height = int(input())
width = int(input())
percent_down = int(input())
total_space_for_painting = math.ceil(4 * (height * width) - (4 * (height * width) * percent_down / 100))
is_all_painted = False

command = input()
while command != "Tired!":

    litres_paint = int(command)
    total_space_for_painting -= litres_paint

    if total_space_for_painting <= 0:
        is_all_painted = True
        break
    command = input()


if is_all_painted:
    difference = total_space_for_painting - litres_paint
    if difference < 0:
        print(f'All walls are painted and you have {abs(total_space_for_painting)} l paint left!')
    elif difference == 0:
        print(f'All walls are painted! Great job, Pesho!')

else:
    print(f"{abs(total_space_for_painting)} quadratic m left." )