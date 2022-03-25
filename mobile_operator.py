contract_duration = input()
contract_type = input()
added_mobile_net = input()
number_of_months_for_paying = int(input())
monthly_tax = 0
taxes_to_be_paid = 0
if contract_duration == 'one':
    if contract_type == 'Small':
        monthly_tax = 9.98
    elif contract_type == 'Middle':
        monthly_tax = 18.99
    elif contract_type == 'Large':
        monthly_tax = 25.98
    elif contract_type == 'ExtraLarge':
        monthly_tax = 35.99
elif contract_duration == 'two':
    if contract_type == 'Small':
        monthly_tax = 8.58
    elif contract_type == 'Middle':
        monthly_tax = 17.09
    elif contract_type == 'Large':
        monthly_tax = 23.59
    elif contract_type == 'ExtraLarge':
        monthly_tax = 31.79

if added_mobile_net == 'yes':
    if monthly_tax <= 10:
        monthly_tax = monthly_tax + 5.50
    elif 10 < monthly_tax <= 30:
        monthly_tax = monthly_tax + 4.35
    elif monthly_tax > 30:
        monthly_tax = monthly_tax + 3.85

taxes_to_be_paid = monthly_tax * number_of_months_for_paying
if contract_duration == 'two':
    taxes_to_be_paid = taxes_to_be_paid - (taxes_to_be_paid * 3.75 / 100)
else:
    taxes_to_be_paid = monthly_tax * number_of_months_for_paying

print (f'{taxes_to_be_paid:.2f} lv.')
