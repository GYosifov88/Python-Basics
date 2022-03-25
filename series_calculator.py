import math

serial_name = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
time_of_normal_episode = float(input())

total_episodes = number_of_episodes * number_of_seasons
adverts_time = time_of_normal_episode * 0.20
total_episodes_times = time_of_normal_episode + adverts_time

special_episodes_time = number_of_seasons * 10

total_time = total_episodes * total_episodes_times + special_episodes_time

print(f'Total time needed to watch the {serial_name} series is {math.floor(total_time)} minutes.')
