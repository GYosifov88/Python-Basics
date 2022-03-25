width = int(input())
lenght = int(input())
full_cake = width * lenght
cake_finished = False
command = input()
while command != 'STOP':
    cake_numbers = int(command)
    full_cake -= cake_numbers

    if full_cake < 0:
        cake_finished = True
        break
    command = input()


number_of_pieces_left = abs(full_cake)

if cake_finished:
    print (f'No more cake left! You need {number_of_pieces_left} pieces more.')

else:
    print (f'{number_of_pieces_left} pieces are left.')

