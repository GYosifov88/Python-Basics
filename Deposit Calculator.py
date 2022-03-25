deposit = float(input())
term_of_deposit = int(input())
interest_percent = float(input())
interest_accumulated = deposit * interest_percent / 100
interest_per_month = interest_accumulated / 12
total_amount = deposit + term_of_deposit * interest_per_month
print(total_amount)