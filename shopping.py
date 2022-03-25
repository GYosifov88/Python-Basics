budget = float(input())
number_videocards = int(input())
number_procesors = int(input())
number_ram_memories = int(input())

price_videocard = 250
sum_videocard = price_videocard * number_videocards
price_processor = sum_videocard * 0.35
price_ram_memorie = sum_videocard * 0.10

total_sum = number_videocards * price_videocard + number_procesors * price_processor + number_ram_memories * price_ram_memorie

if number_videocards > number_procesors:
    total_sum = total_sum - total_sum * 15 / 100

leftover = abs(budget - total_sum)

if budget >= total_sum:
    print (f'You have {leftover:.2f} leva left!')
else:
    print (f'Not enough money! You need {leftover:.2f} leva more!')