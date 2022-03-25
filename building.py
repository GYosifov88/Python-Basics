number_of_floors = int(input())
number_of_rooms = int(input())

for floors in range (number_of_floors, 0, -1):
    for rooms in range (number_of_rooms):
        name_of_room = floors * 10 + rooms
        if floors == number_of_floors:
            print(f'L{name_of_room}', end =" ")
        elif floors % 2 == 0:
            print(f'O{name_of_room}', end = " ")
        else:
            print(f'A{name_of_room}', end=" ")
    print()
