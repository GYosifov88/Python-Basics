top_player = ''
top_score = 0
while True:
    player_name = input()
    current_score = 0

    if player_name == 'Stop':
        break

    for score in range (len(player_name)):
        current_num = int(input())

        if current_num == ord(player_name[score]):
            current_score += 10
        else:
            current_score += 2

    if current_score >= top_score:
        top_player = player_name
        top_score = current_score

print(f"The winner is {top_player} with {top_score} points!")




