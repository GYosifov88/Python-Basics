age = int(input())
laundry_price = float(input())
toy_price = int(input())
saved_money = 0
toy_numbers = 0
birthday_money = 0
for ages in range (1, age + 1):
    if ages % 2 != 0:
        toy_numbers += 1
    else:
        birthday_money += 10
        saved_money += birthday_money - 1

saved_money = saved_money + (toy_price * toy_numbers)

diff = abs(saved_money - laundry_price)

if saved_money >= laundry_price:
    print(f'Yes! {diff:.2f}')
else:
    print (f'No! {diff:.2f} ')