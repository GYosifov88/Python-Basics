number_of_days = int(input())
number_of_hours = int(input())
cost_for_all_period = 0

for day in range (1, number_of_days + 1):
    current_cost = 0
    for hour in range (1, number_of_hours + 1):
        if day % 2 == 0:
            if hour % 2 != 0:
                cost_for_all_period += 2.50
                current_cost += 2.50
            else:
                cost_for_all_period += 1
                current_cost += 1
        elif day % 2 != 0:
            if hour % 2 == 0:
                cost_for_all_period += 1.25
                current_cost += 1.25
            else:
                cost_for_all_period += 1
                current_cost += 1

    print(f'Day: {day} – {current_cost:.2f} leva')
print (f'Total: {cost_for_all_period:.2f} leva')



