import math
grape_field_area = int(input())
grapes_per_sq_meter = float(input())
needed_litres_wine = int(input())
number_of_workers = int(input())

total_grapes = grape_field_area * grapes_per_sq_meter
wine_quantity = total_grapes * 0.4 / 2.5

difference = abs(needed_litres_wine - wine_quantity)
litres_per_worker = abs(wine_quantity - needed_litres_wine) / number_of_workers
if wine_quantity < needed_litres_wine:
    print(f'It will be a tough winter! More {math.floor(difference)} liters wine needed.')
elif wine_quantity >= needed_litres_wine:
    print(f'Good harvest this year! Total wine: {math.floor(wine_quantity)} liters.')
    print(f'{math.ceil(difference)} liters left -> {math.ceil(litres_per_worker)} liters per person.')