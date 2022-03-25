from math import floor
number_of_balls = int(input())
total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
points = 0
other_colours = 0
black_devided = 0
for i in range (number_of_balls):
    balls_colour = input()
    if balls_colour == 'red':
        total_points += 5
        red_balls += 1
    elif balls_colour == 'orange':
        total_points += 10
        orange_balls += 1
    elif balls_colour == 'yellow':
        total_points += 15
        yellow_balls += 1
    elif balls_colour == 'white':
        total_points += 20
        white_balls += 1
    elif balls_colour == 'black':
        total_points = floor(total_points / 2)
        black_devided += 1
        black_balls += 1
    else:
        other_colours += 1

print (f'Total points: {total_points}')
print (f'Points from red balls: {red_balls}')
print (f'Points from orange balls: {orange_balls}')
print (f'Points from yellow balls: {yellow_balls}')
print (f'Points from white balls: {white_balls}')
print (f'Other colors picked: {other_colours}')
print (f'Divides from black balls: {black_devided}')
