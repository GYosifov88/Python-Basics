trunk_capacity = float(input())
is_trunk_full = False
number_of_baggage = 0
command = input()

while command != 'End':
    current_luggage = float(command)
    trunk_capacity -= current_luggage
    number_of_baggage += 1

    if number_of_baggage % 3 == 0:
        trunk_capacity -= current_luggage * 0.1
    if trunk_capacity <= 0:
        is_trunk_full = True
        number_of_baggage -= 1
        break

    command = input()


if is_trunk_full:
    print('No more space!')
    print(f'Statistic: {number_of_baggage} suitcases loaded.')
else:
    print(f'Congratulations! All suitcases are loaded!')
    print(f'Statistic: {number_of_baggage} suitcases loaded.')