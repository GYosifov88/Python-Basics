electricity_bill = 0
water_bill = 20
internet_bill = 15
other_bills = 0
number_of_months = int(input())
total_el = 0
total_water = number_of_months * water_bill
total_net = number_of_months * internet_bill
total_other_bills = 0
for i in range (number_of_months):
    electricity_bill = float(input())
    other_bills = water_bill + internet_bill + electricity_bill + ((water_bill + internet_bill + electricity_bill) * 20 /100)
    total_el +=electricity_bill
    total_other_bills += other_bills

all_expenses = total_net + total_water + total_el + total_other_bills
average = all_expenses / number_of_months


print(f"Electricity: {total_el:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_net:.2f} lv")
print(f"Other: {total_other_bills:.2f} lv")
print(f"Average: {average:.2f} lv")


