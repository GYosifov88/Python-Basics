player_one_name = input()
player_two_name = input()
result_player_one = 0
result_player_two = 0

while True:
    command1 = input()
    if command1 == 'End of game':
        print(f"{player_one_name} has {result_player_one} points")
        print(f"{player_two_name} has {result_player_two} points")
        break

    card_of_first_player = int(command1)
    command2 = input()
    card_of_second_player = int(command2)

    if card_of_first_player > card_of_second_player:
        result_player_one += (card_of_first_player - card_of_second_player)
    elif card_of_second_player > card_of_first_player:
        result_player_two += (card_of_second_player - card_of_first_player)
    elif card_of_first_player == card_of_second_player:
        print ('Number wars!')
        add_card_first_player = int(input())
        add_card_second_player = int(input())
        if add_card_second_player > add_card_first_player:
            print(f"{player_two_name} is winner with {result_player_two} points")
        elif add_card_second_player < add_card_first_player:
            print(f"{player_one_name} is winner with {result_player_one} points")
        break