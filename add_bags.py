price_luggage_over20 = float(input())
luggage_weight = float(input())
days_till_trip = int(input())
number_of_luggages = int(input())
price_luggage = 0
price_per_bag = 0


if luggage_weight < 10:
    price_luggage = (price_luggage_over20 * 20 / 100)
    price_per_bag = price_luggage * number_of_luggages

elif 10 <= luggage_weight <= 20:
    price_luggage = price_luggage_over20 * 50 / 100
    price_per_bag = price_luggage * number_of_luggages

elif luggage_weight > 20:
    price_luggage = price_luggage_over20
    price_per_bag = price_luggage * number_of_luggages

if days_till_trip > 30:
    price_luggage = price_luggage + (price_luggage * 10 / 100)
    price_per_bag = price_luggage * number_of_luggages

elif 7 <= days_till_trip <= 30:
    price_luggage = price_luggage + (price_luggage * 15 / 100)
    price_per_bag = price_luggage * number_of_luggages

elif days_till_trip < 7:
    price_luggage = price_luggage + (price_luggage * 40 / 100)
    price_per_bag = price_luggage * number_of_luggages


print(f'The total price of bags is: {price_per_bag:.2f} lv.')