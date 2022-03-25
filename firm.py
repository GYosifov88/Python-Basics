import math
needed_hours = int(input())
given_days = int(input())
number_of_workers_extra_working = int(input())

worked_days = given_days - (given_days * 0.1)
normal_working_hours = worked_days * 8
extra_hours_worked = number_of_workers_extra_working * 2 * given_days
total_worked = normal_working_hours + extra_hours_worked
difference = abs(needed_hours - total_worked)

if total_worked >= needed_hours:
    print(f'Yes!{math.floor(difference)} hours left.')
else:
    print(f'Not enough time!{math.ceil(difference)} hours needed.')