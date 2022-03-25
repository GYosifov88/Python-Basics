number = int(input())
counter_devided_by_2 = 0
counter_devided_by_3 = 0
counter_devided_by_4 = 0

for i in range (number):
    current_num = int(input())
    if current_num % 2 == 0:
        counter_devided_by_2 += 1
    if current_num % 3 == 0:
        counter_devided_by_3 += 1
    if current_num % 4 == 0:
        counter_devided_by_4 += 1
percent_divided_by_2 = counter_devided_by_2 / number * 100
percent_divided_by_3 = counter_devided_by_3 / number * 100
percent_divided_by_4 = counter_devided_by_4 / number * 100

print(f'{percent_divided_by_2:.2f}%')
print(f'{percent_divided_by_3:.2f}%')
print(f'{percent_divided_by_4:.2f}%')