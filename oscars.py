actor = input()
total_points = float(input())
number_of_jury = int(input())

for i in range (number_of_jury):
    jury_name = input()
    jury_points = float(input())

    total_points = total_points + len(jury_name) * jury_points / 2
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print (f'Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!')
else:
    diff = abs(total_points - 1250.5)
    print (f'Sorry, {actor} you need {diff:.1f} more!')