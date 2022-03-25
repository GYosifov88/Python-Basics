from math import floor
number_of_tournaments = int(input())
starting_points = int(input())
tournament_points = 0
total_points = starting_points + tournament_points
average_points = 0
count_wins = 0
for i in range (number_of_tournaments):
    stage = input()
    if stage == 'W':
        count_wins +=1
        tournament_points = 2000
        total_points += tournament_points
    elif stage == 'F':
        tournament_points = 1200
        total_points += tournament_points
    elif stage == 'SF':
        tournament_points = 720
        total_points += tournament_points


average_points = (total_points - starting_points) / number_of_tournaments
percent_wins = count_wins / number_of_tournaments * 100

print(f'Final points: {total_points}')
print (f'Average points: {floor(average_points)}')
print (f'{percent_wins:.2f}%')