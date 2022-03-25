import sys

number_of_kilometers = int(input())
period_of_day = input()
min_price = sys.maxsize
cost_taxi = 0
cost_bus = 0
cost_train = 0
min_cost = 0
if number_of_kilometers < 20:
    if period_of_day == 'day':
        cost_taxi = 0.70 + number_of_kilometers * 0.79
    elif period_of_day == 'night':
        cost_taxi = 0.70 + number_of_kilometers * 0.90
    min_cost = cost_taxi
elif 20 <= number_of_kilometers < 100:
        cost_bus = number_of_kilometers * 0.09
        if cost_bus < min_price:
            min_cost = cost_bus
elif number_of_kilometers >= 100:
        cost_train = number_of_kilometers * 0.06
        if cost_train < min_price:
            min_cost = cost_train

print(f'{min_cost:.2f}')



