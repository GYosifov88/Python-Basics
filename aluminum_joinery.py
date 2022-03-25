number = int(input())
vid_dograma = str(input())
delivery_type = str(input())
price = 0
cost = 0

if vid_dograma == '90X130':
    price = 110
    cost = number * price
    if 30 < number <= 60:
        cost = cost - (cost * 5 / 100)

    elif number > 60:
        cost = cost - (cost * 8 / 100)

elif vid_dograma == '100X150':
    price = 140
    cost = number * price
    if 40 < number <= 80:
        cost = cost - (cost * 6 / 100)

    elif number > 80:
        cost = cost - (cost * 10 / 100)

elif vid_dograma == '130X180':
    price = 190
    cost = number * price
    if 20 < number <= 50:
        cost = cost - (cost * 7 / 100)

    elif number > 50:
        cost = cost - (cost * 12 / 100)

elif vid_dograma == '200X300':
    price = 250
    cost = number * price
    if 25 < number <= 50:
        cost = cost - (cost * 9 / 100)

    elif number > 50:
        cost = cost - (cost * 14 / 100)

if delivery_type == 'With delivery':
  cost = cost + 60

elif delivery_type == 'Without delivery':
    cost = cost

if number >= 99:
    cost = cost - (cost * 4 / 100)

if number >= 10:
    print(f'{cost:.2f} BGN')
else:
    print('Invalid order')