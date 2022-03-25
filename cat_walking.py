minutes_walk = int(input())
number_of_walks = int(input())
calories_daily = int(input())

total_minutes_walk = minutes_walk * number_of_walks

calories_burned = abs(total_minutes_walk * 5)

if calories_burned >= calories_daily / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.')