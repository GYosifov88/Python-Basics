actor_name = input()
starting_points = float(input())
number_of_jury = int(input())
total_points = 0

for i in range (number_of_jury):
    jury_name = input()
    jury_points = float(input())
    current_points = len(jury_name) * jury_points / 2
    total_points += current_points
    final_points = starting_points + total_points
    if final_points >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {final_points:.1f}!')
        break

difference = abs(1250.5 - final_points)

# if final_points >= 1250.5:
#         print(f'Congratulations, {actor_name} got a nominee for leading role with {final_points:.1f}!')
if final_points < 1250.5:
        print(f'Sorry, {actor_name} you need {difference:.1f} more!')