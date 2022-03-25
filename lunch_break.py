import math

name_serial = str(input())
time_episode = int(input())
time_break = int(input())

time_lunch = time_break * 1 / 8
time_rest = time_break * 1 / 4

time_left = abs(time_break - time_lunch - time_rest)
minutes_left = abs(time_left - time_episode)

if time_left >= time_episode:
    print(f'You have enough time to watch {name_serial} and left with {math.ceil(minutes_left)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_serial}, you need {math.ceil(minutes_left)} more minutes.")
