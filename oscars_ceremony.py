hall_rent = int(input())

statues_price = hall_rent - (hall_rent * 30 / 100)
cetaring = statues_price - (statues_price * 15 / 100)
sound = cetaring / 2

cost = statues_price + hall_rent + cetaring + sound

print (f'{cost:.2f}')