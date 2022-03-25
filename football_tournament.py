team_name = input()
number_of_games = int(input())
number_of_wins = 0
number_of_draws = 0
number_of_loses = 0
points_gain = 0

for games in range (1, number_of_games + 1):
    result = input()
    if result == 'W':
        number_of_wins += 1
        points_gain += 3
    if result == 'D':
        number_of_draws += 1
        points_gain += 1
    if result == 'L':
        number_of_loses += 1


if number_of_games < 1:
    print(f"{team_name} hasn't played any games during this season.")

elif number_of_games >= 1:
    percent_wins = number_of_wins / number_of_games * 100
    print(f"{team_name} has won {points_gain} points during this season.")
    print('Total stats:')
    print(f'## W: {number_of_wins}')
    print(f'## D: {number_of_draws}')
    print(f'## L: {number_of_loses}')
    print(f'Win rate: {percent_wins:.2f}%')