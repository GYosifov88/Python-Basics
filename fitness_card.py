budget = float(input())
gender = input()
age = int(input())
sport = input()
card_price = 0
if sport == 'Gym':
    if gender == 'm':
        card_price = 42
    elif gender == 'f':
        card_price = 35
elif sport == 'Boxing':
    if gender == 'm':
        card_price = 41
    elif gender == 'f':
        card_price = 37
elif sport == 'Yoga':
    if gender == 'm':
        card_price = 45
    elif gender == 'f':
        card_price = 42
elif sport == 'Zumba':
    if gender == 'm':
        card_price = 34
    elif gender == 'f':
        card_price = 31
elif sport == 'Dances':
    if gender == 'm':
        card_price = 51
    elif gender == 'f':
        card_price = 53
elif sport == 'Pilates':
    if gender == 'm':
        card_price = 39
    elif gender == 'f':
        card_price = 37

if age <= 19:
    card_price = card_price - (card_price * 20 / 100)
else:
    card_price = card_price

difference = abs(budget - card_price)

if budget >= card_price:
    print(f'You purchased a 1 month pass for {sport}.')
elif budget < card_price:
    print(f"You don't have enough money! You need ${difference:.2f} more.")