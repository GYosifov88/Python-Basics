budget = float(input())
number_of_nights = int(input())
night_price = float(input())
percent_extra_costs = int(input())

if number_of_nights > 7:
    night_price = night_price - (night_price * 0.05)

night_cost = night_price * number_of_nights
extra_costs = budget * (percent_extra_costs / 100)

total_cost = night_cost + extra_costs
diff = abs (budget - total_cost)
if total_cost <= budget:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')