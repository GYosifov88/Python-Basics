import math

shooting_time = int(input())
number_of_scenes = int(input())
scene_time = int(input())

terrain_prepare = shooting_time * 15 / 100
total_scene_time = number_of_scenes * scene_time

total_time = total_scene_time + terrain_prepare
difference = abs(total_time - shooting_time)
if shooting_time >= total_time:
    print (f'You managed to finish the movie on time! You have {round(difference)} minutes left!')
else:
    print (f'Time is up! To complete the movie you need {round(difference)} minutes.')
