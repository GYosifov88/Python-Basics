number_of_sugar_bread = int(input())
number_of_egg_carboard = int(input())
kilos_of_cookies = int(input())

cost_of_sugar_breads = number_of_sugar_bread * 3.20
cost_of_cookies = kilos_of_cookies * 5.40
number_of_eggs = number_of_egg_carboard * 12
cost_of_egg_carboards = number_of_egg_carboard * 4.35
cost_of_egg_painting = number_of_eggs * 0.15

total_cost = cost_of_cookies + cost_of_sugar_breads + cost_of_egg_carboards + cost_of_egg_painting

print (f'{total_cost:.2f}')