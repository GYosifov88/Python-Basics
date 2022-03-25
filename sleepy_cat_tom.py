number_of_non_working_days = int(input())

working_days = 365 - number_of_non_working_days
tom_norm_for_playing = 30000
playing_time_non_working_days = number_of_non_working_days * 127
playing_time_working_days = working_days * 63
total_playing_time = playing_time_working_days + playing_time_non_working_days

difference = abs(tom_norm_for_playing - total_playing_time)
diff_hours = difference // 60
diff_min = difference % 60
if total_playing_time > tom_norm_for_playing:
    print('Tom will run away')
    print(f'{diff_hours} hours and {diff_min} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{diff_hours} hours and {diff_min} minutes less for play')