period_of_time = int(input())
treated_pacients = 0
untreated_pacients = 0
number_of_doctors = 7
new_doctors = 0
for days in range (1, period_of_time + 1):
    if days % 3 == 0 and treated_pacients < untreated_pacients:
        number_of_doctors += 1
    number_of_pacients = int(input())

    if number_of_doctors >= number_of_pacients:
        treated_pacients += number_of_pacients
        # untreated_pacients += number_of_pacients - treated_pacients

    else:
        treated_pacients += number_of_doctors
        untreated_pacients += number_of_pacients - number_of_doctors


print(f"Treated patients: {treated_pacients}.")
print(f"Untreated patients: {untreated_pacients}.")


