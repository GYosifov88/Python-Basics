screening_type = input()
rows = int(input())
columns = int(input())
income = 0
tickets_price = 0
cinema_capacity = rows * columns
if screening_type == 'Premiere':
 tickets_price = 12
 income = cinema_capacity * tickets_price
elif screening_type == 'Normal':
 tickets_price = 7.50
 income = cinema_capacity * tickets_price
elif screening_type == 'Discount':
 tickets_price = 5
 income = cinema_capacity * tickets_price

print(f'{income:.2f} leva')