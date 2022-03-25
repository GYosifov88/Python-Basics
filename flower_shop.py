import math

number_of_magnolia = int(input())
number_of_zumbuls = int(input())
number_of_roses = int(input())
number_of_cactuses = int(input())
gift_price = float(input())

magnolia_price = number_of_magnolia * 3.25
zumbuls_price = number_of_zumbuls * 4
roses_price = number_of_roses * 3.5
cactuses_price = number_of_cactuses * 8

flower_gain = magnolia_price + zumbuls_price + roses_price + cactuses_price

final_gain = flower_gain - (flower_gain * 0.05)

difference = abs(final_gain - gift_price)

if final_gain >= gift_price:
    print (f'She is left with {math.floor(difference)} leva.')
else:
    print(f'She will have to borrow {math.ceil(difference)} leva.')