player_name = input()
result = 301
successful_shots = 0
unsuccessful_shots = 0
is_result_matched = False

while True:
    command = input()
    if command == 'Retire':
        print (f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break
    points = int(input())
    if command == 'Single':
        points = points
        result -= points
        successful_shots +=1
    elif command == 'Double':
        points *= 2
        result -= points
        successful_shots += 1
    elif command == 'Triple':
        points *= 3
        result -= points
        successful_shots += 1
    if points > result:
        unsuccessful_shots += 1

    if result == 0:
        is_result_matched = True
        print (f"{player_name} won the leg with {successful_shots} shots.")
        break



