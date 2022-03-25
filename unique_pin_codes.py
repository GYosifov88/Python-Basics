upper_limit_first_digit = int(input())
upper_limit_second_digit = int(input())
upper_limit_third_digit = int(input())
is_pin_valid = False
number1 = 0
number2 = 0
number3 = 0
is_digit_good = False

for num1 in range (2, upper_limit_first_digit + 1, 2):
    for num2 in range (2, upper_limit_second_digit + 1):
        for num3 in range (2, upper_limit_third_digit + 1, 2):
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                print(f"{num1} {num2} {num3}")

