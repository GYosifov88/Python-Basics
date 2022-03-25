from math import floor
record_climbing = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

george_time = distance_meters * seconds_per_meter
slowing = floor(distance_meters // 50) * 30
total_time = george_time + slowing

difference = abs(total_time - record_climbing)

if total_time < record_climbing:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {difference:.2f} seconds slower.')