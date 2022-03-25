number_of_clients = int(input())
number_of_baskets = 0
number_of_wreaths = 0
number_of_chocolate_bunnies = 0
overall_cost = 0
for clients in range (number_of_clients):
    cost = 0
    total_purchasing = 0

    while True:
        purchased_product = input()

        if purchased_product == 'Finish':
            if total_purchasing % 2 == 0:
                cost = cost - (cost * 0.2)
            print(f"You purchased {total_purchasing} items for {cost:.2f} leva.")
            break

        if purchased_product == 'basket':
            number_of_baskets += 1
            cost += 1.50
        elif purchased_product == 'wreath':
            number_of_wreaths += 1
            cost += 3.80
        elif purchased_product == 'chocolate bunny':
            number_of_chocolate_bunnies += 1
            cost += 7

        total_purchasing += 1
    overall_cost += cost

average_cost = overall_cost / number_of_clients

print(f"Average bill per client is: {average_cost:.2f} leva.")



