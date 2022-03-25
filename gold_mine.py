number_of_locations = int(input())

for locations in range (number_of_locations):
    total_digged = 0
    estimated_average_earn_of_gold = float (input())
    number_of_days_to_dig_at_location = int(input())
    for days in range (number_of_days_to_dig_at_location):
        digged_gold_for_the_day = float(input())
        total_digged += digged_gold_for_the_day
        average_digged = total_digged / number_of_days_to_dig_at_location

        difference = abs(average_digged - estimated_average_earn_of_gold)

    if average_digged >= estimated_average_earn_of_gold:
        print (f"Good job! Average gold per day: {average_digged:.2f}.")
    else:
        print (f"You need {difference:.2f} gold.")