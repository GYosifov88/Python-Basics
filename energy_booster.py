fruit = input()
size = input()
number_of_sets = int(input())
price = 0
set_price = 0
if fruit == 'Watermelon':
     if size == 'small':
         price = 56 * 2
         set_price = number_of_sets * price
     elif size == 'big':
         price = 28.70 * 5
         set_price = number_of_sets * price
elif fruit == 'Mango':
     if size == 'small':
         price = 36.66 * 2
         set_price = number_of_sets * price
     elif size == 'big':
         price = 19.60 * 5
         set_price = number_of_sets * price
elif fruit == 'Pineapple':
     if size == 'small':
         price = 42.10 * 2
         set_price = number_of_sets * price
     elif size == 'big':
         price = 24.80 * 5
         set_price = number_of_sets * price
elif fruit == 'Raspberry':
     if size == 'small':
         price = 20 * 2
         set_price = number_of_sets * price
     elif size == 'big':
         price = 15.20 * 5
         set_price = number_of_sets * price

if 400 <= set_price <= 1000:
    set_price = set_price - (set_price * 15 / 100)
elif set_price > 1000:
    set_price = set_price - (set_price * 50 / 100)

print(f'{set_price:.2f} lv.')