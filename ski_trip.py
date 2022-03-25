days = int(input())
type_of_room = input()
feedback = input()
price = 0
nights = days - 1


if type_of_room == 'room for one person':
    price = 18
    cost = nights * price
elif type_of_room == 'apartment':
    price = 25
    cost = nights * price
    if days < 10:
        cost = cost - (cost * 30 /100)
    elif 10 <= days <= 15:
        cost = cost - (cost * 35 / 100)
    elif days > 15:
        cost = cost - (cost * 50 / 100)
elif type_of_room == 'president apartment':
    price = 35
    cost = nights * price
    if days < 10:
        cost = cost - (cost * 10 /100)
    elif 10 <= days <= 15:
        cost = cost - (cost * 15 / 100)
    elif days > 15:
        cost = cost - (cost * 20 / 100)

if feedback == 'positive':
    cost = cost + (cost * 25 /100)
elif feedback == 'negative':
    cost = cost - (cost * 10 / 100)

print (f'{cost:.2f}')