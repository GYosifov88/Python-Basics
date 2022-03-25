room_capacity = int(input())
is_room_full = False
total_people = 0
ticket_price = 5
gain = 0
command = input()

while command != 'Movie time!':
    number_of_people = int(command)
    total_people += number_of_people
    tickets_cost = number_of_people * ticket_price

    if number_of_people % 3 == 0:
        tickets_cost = number_of_people * ticket_price - 5

    else:
        tickets_cost = number_of_people * ticket_price

    if total_people > room_capacity:
        is_room_full = True
        break
    gain += tickets_cost

    command = input()

seats_left = abs(room_capacity - total_people)
if is_room_full :
    print('The cinema is full.')
    print(f'Cinema income - {gain} lv.')
else:
    print(f'There are {seats_left} seats left in the cinema.')
    print(f'Cinema income - {gain} lv.')

