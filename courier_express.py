weight_of_delivery_kg = float(input())
service_type = input()
distance_km = int(input())
price_per_km = 0
cost = 0
if service_type == 'standard':
    if weight_of_delivery_kg < 1:
        price_per_km = 0.03
        cost = price_per_km * distance_km
    elif  1 <= weight_of_delivery_kg < 10:
        price_per_km = 0.05
        cost = price_per_km * distance_km
    elif  10 <= weight_of_delivery_kg < 40:
        price_per_km = 0.10
        cost = price_per_km * distance_km
    elif  40 <= weight_of_delivery_kg < 90:
        price_per_km = 0.15
        cost = price_per_km * distance_km
    elif  90 <= weight_of_delivery_kg < 150:
        price_per_km = 0.20
        cost = price_per_km * distance_km
elif service_type == 'express':
    if weight_of_delivery_kg < 1:
        price_per_km = 0.03
        extra = 0.03 * 80 / 100 * weight_of_delivery_kg
        cost = (price_per_km * distance_km) + (distance_km * extra)
    elif  1 <= weight_of_delivery_kg < 10:
        price_per_km = 0.05
        extra = 0.05 * 40 / 100 * weight_of_delivery_kg
        cost = (price_per_km * distance_km) + (distance_km * extra)
    elif  10 <= weight_of_delivery_kg < 40:
        price_per_km = 0.10
        extra = 0.10 * 5 / 100 * weight_of_delivery_kg
        cost = (price_per_km * distance_km) + (distance_km * extra)
    elif  40 <= weight_of_delivery_kg < 90:
        price_per_km = 0.15
        extra = 0.15 * 2 / 100 * weight_of_delivery_kg
        cost = (price_per_km * distance_km) + (distance_km * extra)
    elif  90 <= weight_of_delivery_kg < 150:
        price_per_km = 0.20
        extra = 0.20 * 1 / 100 * weight_of_delivery_kg
        cost = (price_per_km * distance_km) + (distance_km * extra)

print(f'The delivery of your shipment with weight of {weight_of_delivery_kg:.3f} kg. would cost {cost:.2f} lv.')