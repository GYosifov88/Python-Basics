budget = float (input())
number_of_serials = int(input())
serials_cost = 0
for i in range (number_of_serials):
    serial_name = input()
    serial_price = float(input())
    if serial_name == "Thrones":
        serial_price = serial_price - (serial_price * 50 / 100)
        serials_cost += serial_price
    elif serial_name == "Lucifer":
        serial_price = serial_price - (serial_price * 40 / 100)
        serials_cost += serial_price
    elif serial_name == "Protector":
        serial_price = serial_price - (serial_price * 30 / 100)
        serials_cost += serial_price
    elif serial_name == "TotalDrama":
        serial_price = serial_price - (serial_price * 20 / 100)
        serials_cost += serial_price
    elif serial_name == "Area":
        serial_price = serial_price - (serial_price * 10 / 100)
        serials_cost += serial_price
    else:
        serial_price = serial_price
        serials_cost += serial_price

difference = abs(budget - serials_cost)

if budget >= serials_cost:
    print (f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")