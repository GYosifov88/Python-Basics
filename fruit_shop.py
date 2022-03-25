fruit = input()
day_of_week = input()
quantity = float(input())
price = 0
condition = True
if day_of_week in ('Monday' 'Tuesday' 'Wednesday' 'Thursday' 'Friday'):
    if fruit == 'banana':
        price = 2.50
    if fruit == 'apple':
        price = 1.20
    if fruit == 'orange':
        price = 0.85
    if fruit == 'grapefruit':
        price = 1.45
    if fruit == 'kiwi':
        price = 2.70
    if fruit == 'pineapple':
        price = 5.50
    if fruit == 'grapes':
        price = 3.85

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    if fruit == 'apple':
        price = 1.25
    if fruit == 'orange':
        price = 0.90
    if fruit == 'grapefruit':
        price = 1.60
    if fruit == 'kiwi':
        price = 3.00
    if fruit == 'pineapple':
        price = 5.60
    if fruit == 'grapes':
        price = 4.20

total_price = quantity * price
if price !=0:
 print (f'{total_price:.2f}')
else:
    print('error')
