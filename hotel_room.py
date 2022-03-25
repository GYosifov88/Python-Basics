month = input()
number_of_days = int(input())
price_per_night_studio = 0
price_per_night_apartment = 0
total_price_studio = number_of_days * price_per_night_studio
total_price_apartment = number_of_days * price_per_night_apartment
if month == 'May' or month == 'October':
    price_per_night_studio = 50
    price_per_night_apartment = 65
    if 7 < number_of_days < 14 :
        price_per_night_studio = price_per_night_studio - (price_per_night_studio * 5 / 100)
    if number_of_days > 14:
        price_per_night_studio = price_per_night_studio - (price_per_night_studio * 30 / 100)
        price_per_night_apartment = price_per_night_apartment - (price_per_night_apartment * 10 / 100)

elif month == 'June' or month == 'September':
    price_per_night_studio = 75.20
    price_per_night_apartment = 68.70
    if number_of_days > 14:
        price_per_night_studio = price_per_night_studio - (price_per_night_studio * 20 / 100)
        price_per_night_apartment = price_per_night_apartment - (price_per_night_apartment * 10 / 100)
elif month == 'July' or month == 'August':
    price_per_night_studio = 76
    price_per_night_apartment = 77
    if number_of_days > 14:
        price_per_night_apartment = price_per_night_apartment - (price_per_night_apartment * 10 / 100)

total_price_studio = number_of_days * price_per_night_studio
total_price_apartment = number_of_days * price_per_night_apartment

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')
