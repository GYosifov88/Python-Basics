name_air_company = str(input())
number_tickets_adults = int(input())
number_tickets_children = int(input())
net_price_ticket_adult = float(input())
tax_processing = float(input())

net_price_ticket_children = net_price_ticket_adult - net_price_ticket_adult * 0.7

price_ticket_children = net_price_ticket_children + tax_processing
price_ticket_adult = net_price_ticket_adult + tax_processing
total_price_tickets = number_tickets_adults * price_ticket_adult + number_tickets_children * price_ticket_children
profit_agency = total_price_tickets * 0.2

print(f'The profit of your agency from {name_air_company} tickets is {profit_agency:.2f} lv.')