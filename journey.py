budget = float(input())
season = input()
cost = 0
destination = ''
accomodation = ''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        cost = budget * 30 / 100
        accomodation = 'Camp'
    elif season == 'winter':
        cost = budget * 70 / 100
        accomodation = 'Hotel'
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        cost = budget * 40 / 100
        accomodation = 'Camp'
    elif season == 'winter':
        cost = budget * 80 / 100
        accomodation = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    cost = budget * 90 / 100
    accomodation = 'Hotel'

print (f'Somewhere in {destination}')
print (f'{accomodation} - {cost:.2f}')
