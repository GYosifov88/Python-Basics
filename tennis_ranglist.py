import math

number_of_tournaments = int(input())
starting_points = int(input())
accumulated_points = 0
number_of_wins = 0

for i in range (number_of_tournaments):
    tournament_stage = input()
    if tournament_stage == 'W':
        points = 2000
        accumulated_points += 2000
        number_of_wins +=1
    elif tournament_stage == 'F':
        points = 1200
        accumulated_points += 1200
    elif tournament_stage == 'SF':
        points = 720
        accumulated_points += 720
final_points = starting_points + accumulated_points
average_points = math.floor(accumulated_points / number_of_tournaments)
percent_wins = (number_of_wins / number_of_tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_wins:.2f}%")

