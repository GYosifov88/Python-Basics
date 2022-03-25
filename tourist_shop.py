budget = float(input())
needed_funds = 0
product = input()
counter = 0
total_price = 0
is_budget_over = False
while product != 'Stop':
    counter += 1
    product_price = float(input())

    if counter % 3 == 0:
        product_price = product_price / 2

    if budget < product_price:
        is_budget_over = True
        break

    total_price += product_price
    budget -= product_price

    product = input()

needed_funds = abs(budget - product_price)
if is_budget_over:
    print(f"You don't have enough money!")
    print(f"You need {needed_funds:.2f} leva!")
else:
    print(f"You bought {counter} products for {total_price:.2f} leva.")

