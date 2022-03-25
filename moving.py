width = int(input())
lenght = int(input())
height = int(input())
full_space = width * lenght * height
is_room_finished = False

command = input()

while command != 'Done':
    number_boxes = int(command)
    full_space -= number_boxes

    if full_space < 0:
        is_room_finished = True
        break
    command = input()

space_left = abs(full_space)

if is_room_finished:
    print (f'No more free space! You need {space_left} Cubic meters more.')

else:
    print (f'{space_left} Cubic meters left.')