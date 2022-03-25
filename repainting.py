plastic = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())
amount_plastic = (plastic + 2) * 1.50
amount_paint = (paint + paint * 0.10) * 14.50
amount_thinner = thinner * 5.00
plastic_bag = 0.40
materials = amount_thinner + amount_paint + amount_plastic + plastic_bag
workers = (materials * 0.30) * work_hours
total_amount = materials + workers
print(total_amount)

