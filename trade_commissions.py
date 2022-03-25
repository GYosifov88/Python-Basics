city = input()
sales = float(input())
commision = 0

if city == 'Sofia':
    if 0 <= sales <= 500:
        commision = 0.05
    elif 500 < sales <= 1000:
        commision = 0.07
    elif 1000 < sales <= 10000:
        commision = 0.08
    elif sales > 10000:
        commision = 0.12
elif city == 'Varna':
    if 0 <= sales <= 500:
        commision = 0.045
    elif 500 < sales <= 1000:
        commision = 0.075
    elif 1000 < sales <= 10000:
        commision = 0.1
    elif sales > 10000:
        commision = 0.13
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commision = 0.055
    elif 500 < sales <= 1000:
        commision = 0.08
    elif 1000 < sales <= 10000:
        commision = 0.12
    elif sales > 10000:
        commision = 0.145

income = sales * commision
if commision !=0:
    print(f'{income:.2f}')
else:
    print('error')