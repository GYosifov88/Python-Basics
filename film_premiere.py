movie = input()
package = input()
number_of_tickets = int(input())
price_per_ticket = 0
if movie == 'John Wick':
    if package == 'Drink':
        price_per_ticket = 12
    elif package == 'Popcorn':
        price_per_ticket = 15
    elif package == 'Menu':
        price_per_ticket = 19
elif movie == 'Star Wars':
    if package == 'Drink':
        price_per_ticket = 18
    elif package == 'Popcorn':
        price_per_ticket = 25
    elif package == 'Menu':
        price_per_ticket = 30
elif movie == 'Jumanji':
    if package == 'Drink':
        price_per_ticket = 9
    elif package == 'Popcorn':
        price_per_ticket = 11
    elif package == 'Menu':
        price_per_ticket = 14

total_cost = price_per_ticket * number_of_tickets

if movie == 'Star Wars' and number_of_tickets >= 4:
    total_cost = total_cost - (total_cost * 0.3)

if movie == 'Jumanji' and number_of_tickets == 2:
    total_cost = total_cost - (total_cost * 15 / 100)

print (f'Your bill is {total_cost:.2f} leva.')