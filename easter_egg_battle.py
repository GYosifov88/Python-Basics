number_of_eggs_player_one = int(input())
number_of_eggs_player_two = int(input())



while True:
    command = input()
    if command == 'End of battle':
        print(f"Player one has {number_of_eggs_player_one} eggs left.")
        print(f"Player two has {number_of_eggs_player_two} eggs left.")
        break

    if command == 'one':
        number_of_eggs_player_two -= 1
    elif command == 'two':
        number_of_eggs_player_one -= 1

    if number_of_eggs_player_one == 0 or number_of_eggs_player_two == 0:
        break


if number_of_eggs_player_one == 0:
    print (f"Player one is out of eggs. Player two has {number_of_eggs_player_two} eggs left.")
elif number_of_eggs_player_two == 0:
    print (f"Player two is out of eggs. Player one has {number_of_eggs_player_one} eggs left.")