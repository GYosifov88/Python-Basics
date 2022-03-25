destination = input()
dates_of_excursion = input()
number_of_nights = int(input())
price_per_night = 0
if destination == "France":
    if dates_of_excursion == '21-23':
        price_per_night = 30
    elif dates_of_excursion == '24-27':
        price_per_night = 35
    elif dates_of_excursion == '28-31':
        price_per_night = 40
elif destination == "Italy":
    if dates_of_excursion == '21-23':
        price_per_night = 28
    elif dates_of_excursion == '24-27':
        price_per_night = 32
    elif dates_of_excursion == '28-31':
        price_per_night = 39
elif destination == "Germany":
    if dates_of_excursion == '21-23':
        price_per_night = 32
    elif dates_of_excursion == '24-27':
        price_per_night = 37
    elif dates_of_excursion == '28-31':
        price_per_night = 43
excursion_cost = price_per_night * number_of_nights

print(f"Easter trip to {destination} : {excursion_cost:.2f} leva.")