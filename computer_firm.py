number_of_computers = int(input())
number_of_sales = 0
real_sales = 0
made_sales = 0
counter_sales = 0

total_ratings = 0
for i in range (number_of_computers):
    rating = int(input())
    rating_scale = rating % 10
    possible_sales = rating // 10
    total_ratings += rating_scale
    if rating_scale == 2:
        real_sales = possible_sales * 0 / 100
        counter_sales += real_sales
    elif rating_scale == 3:
        real_sales = possible_sales * 50 / 100
        counter_sales += real_sales
    elif rating_scale == 4:
        real_sales = possible_sales * 70 / 100
        counter_sales += real_sales
    elif rating_scale == 5:
        real_sales = possible_sales * 85 / 100
        counter_sales += real_sales
    elif rating_scale == 6:
        real_sales = possible_sales * 100 / 100
        counter_sales += real_sales

average_rating = total_ratings / number_of_computers

print (f'{counter_sales:.2f}')
print (f'{average_rating:.2f}')





