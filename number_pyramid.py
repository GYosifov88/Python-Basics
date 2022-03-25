number = int(input())
counter = 1
is_current_number_bigger_than_number = False
for row in range (1, number + 1):
    for column in range (1, row +1):
        print(counter, end = ' ')
        counter += 1
        if counter > number:
            is_current_number_bigger_than_number = True
            break

    if is_current_number_bigger_than_number:
        break
    print()