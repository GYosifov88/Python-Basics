price_per_kilo_flour = float(input())
kilos_of_flour = float(input())
kilos_of_sugar = float(input())
number_of_egg_cardboards = int(input())
packets_of_eest = int(input())

price_of_kilo_sugar = price_per_kilo_flour - (price_per_kilo_flour * 25 / 100)
price_of_egg_cardboard = price_per_kilo_flour + (price_per_kilo_flour * 0.1)
price_of_packet_eest = price_of_kilo_sugar - price_of_kilo_sugar * 0.8

cost_of_flour = kilos_of_flour * price_per_kilo_flour
cost_of_sugar = kilos_of_sugar * price_of_kilo_sugar
cost_of_eggs = number_of_egg_cardboards * price_of_egg_cardboard
cost_of_eest = packets_of_eest * price_of_packet_eest

total_cost = cost_of_eest + cost_of_eggs + cost_of_sugar + cost_of_flour

print (f'{total_cost:.2f}')