rent = float(input())

cake = rent * 20 / 100
drinks = cake - (cake * 45 / 100)
animator = rent / 3

needed_amount = rent + cake + drinks + animator

print(needed_amount)
