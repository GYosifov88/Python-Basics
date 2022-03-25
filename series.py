budget = float(input())
number_of_serials = int(input())
is_budget_finished = False
serial_name = ''
serial_price = 0
total_price = 0

for i in range (number_of_serials):
    serial_name = input()
    serial_price = float(input())

    if serial_name == 'Thrones':
        serial_price = serial_price - (serial_price * 0.5)
    elif serial_name == 'Lucifer':
        serial_price = serial_price - (serial_price * 0.4)
    elif serial_name == 'Protector':
        serial_price = serial_price - (serial_price * 0.3)
    elif serial_name == 'TotalDrama':
        serial_price = serial_price - (serial_price * 0.2)
    elif serial_name == 'Area':
        serial_price = serial_price - (serial_price * 0.1)

    total_price += serial_price
difference = abs(budget - total_price)

if budget >= total_price:
    print(f'You bought all the series and left with {difference:.2f} lv.')
else:
    print(f'You need {difference:.2f} lv. more to buy the series!')