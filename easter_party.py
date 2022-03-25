number_of_guests = int(input())
price_per_person = float(input())
budget = float(input())
restorant_cost = 0
if 10 <= number_of_guests <= 15:
    price_per_person = price_per_person - price_per_person * 0.15
elif 15 < number_of_guests <= 20:
    price_per_person = price_per_person - price_per_person * 0.2
elif number_of_guests > 20:
    price_per_person = price_per_person - price_per_person * 0.25

restorant_cost = number_of_guests * price_per_person
cake_cost = budget * 0.1
total_cost = restorant_cost + cake_cost

difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")