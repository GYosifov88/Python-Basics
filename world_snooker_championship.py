championship_stage = input()
ticket_type = input()
number_of_tickets = int(input())
picture_with_trophy = input()
total_price = 0

if championship_stage == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_price = 55.50
        total_price = ticket_price * number_of_tickets
    elif ticket_type == 'Premium':
        ticket_price = 105.20
        total_price = ticket_price * number_of_tickets
    elif ticket_type == 'VIP':
        ticket_price = 118.90
        total_price = ticket_price * number_of_tickets
elif championship_stage == 'Semi final':
    if ticket_type == 'Standard':
        ticket_price = 75.88
        total_price = ticket_price * number_of_tickets
    elif ticket_type == 'Premium':
        ticket_price = 125.22
        total_price = ticket_price * number_of_tickets
    elif ticket_type == 'VIP':
        ticket_price = 300.40
        total_price = ticket_price * number_of_tickets
elif championship_stage == 'Final':
    if ticket_type == 'Standard':
        ticket_price = 110.10
        total_price = ticket_price * number_of_tickets
    elif ticket_type == 'Premium':
        ticket_price = 160.66
        total_price = ticket_price * number_of_tickets
    elif ticket_type == 'VIP':
        ticket_price = 400
        total_price = ticket_price * number_of_tickets



if 2500 < total_price <= 4000 and picture_with_trophy == 'Y':
    total_price = total_price - (total_price * 0.1) + number_of_tickets * 40
elif 2500 < total_price <= 4000 and picture_with_trophy == 'N':
    total_price = total_price - (total_price * 0.1)
elif total_price > 4000 and picture_with_trophy == 'Y':
    total_price = total_price - (total_price * 25 / 100)
elif total_price > 4000 and picture_with_trophy == 'N':
    total_price = total_price - (total_price * 25 / 100)
elif total_price <= 2500 and picture_with_trophy == 'Y':
    total_price = total_price + number_of_tickets * 40
elif total_price <= 2500 and picture_with_trophy == 'N':
    total_price = total_price



print(f'{total_price:.2f}')