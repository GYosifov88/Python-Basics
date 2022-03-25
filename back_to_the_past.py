inherit_money = float(input())
year_to_live_to = int(input())
money_left = 0
money_spent = 0
years = 17
for year in range (1800, year_to_live_to + 1):
    years += 1
    if year % 2 == 0:
        money_spent += 12000
    else:
        money_spent += (years * 50 + 12000)
money_left = inherit_money - money_spent
difference = abs(inherit_money - money_spent)

if inherit_money >= money_spent:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive." )