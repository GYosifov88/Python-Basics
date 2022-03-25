minutes_to_reach = int(input())
seconds_to_reach = int(input())
lenght_meters = float(input())
seconds_per_100_meters = int(input())

total_seconds_to_reach = seconds_to_reach + (minutes_to_reach * 60)
time_of_delay = lenght_meters / 120
seconds_of_delay = time_of_delay * 2.5

time_of_athlete = (lenght_meters / 100) * seconds_per_100_meters - seconds_of_delay
difference = abs(time_of_athlete-total_seconds_to_reach)
if time_of_athlete <= total_seconds_to_reach:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_of_athlete:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
