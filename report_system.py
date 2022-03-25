amount_of_sales = int(input())
is_amount_gathered = False
amount_gathered = 0
counter = 0
cash_gathered = 0
card_gathered = 0
cash_counter = 0
card_counter = 0
command = input()

while command != 'End':
    amount_paid = int(command)
    counter += 1
    if counter % 2 == 0 and amount_paid >= 10:
        print("Product sold!")
        amount_gathered += amount_paid
        card_gathered += amount_paid
        card_counter += 1

    elif counter % 2 !=0 and amount_paid <= 100:
        print("Product sold!")
        amount_gathered += amount_paid
        cash_gathered += amount_paid
        cash_counter += 1

    else:
        print("Error in transaction!")

    if amount_gathered >= amount_of_sales:
        is_amount_gathered = True
        average_cash = cash_gathered / cash_counter
        average_card = card_gathered / card_counter
        print(f"Average CS: {average_cash:.2f}")
        print(f"Average CC: {average_card:.2f}")
        break

    command = input()

if not is_amount_gathered:
    print ("Failed to collect required money for charity.")