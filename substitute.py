start_of_interval_first_digit_of_first_number = int(input())
start_of_interval_second_digit_of_first_number = int(input())
start_of_interval_first_digit_of_second_number = int(input())
start_of_interval_second_digit_of_second_number = int(input())
counter = 0
currentnumber1 = 0
currentnumber2 = 0
number1int =0
number2int = 0
is_combination_valid = False
for num1 in range (start_of_interval_first_digit_of_first_number, 8 + 1):
    num1str = str(num1)
    for num2 in range (9, start_of_interval_second_digit_of_first_number, -1):
        num2str = str(num2)
        for num3 in range (start_of_interval_first_digit_of_second_number, 8 + 1):
            num3str = str(num3)
            for num4 in range (9, start_of_interval_second_digit_of_second_number, -1):
                num4str = str(num4)

                number1str = num1str + num2str
                number2str = num3str + num4str
                number1int = int(number1str)
                number2int = int(number2str)
                if (num1 % 2 == 0 and num2 % 2 != 0) and (num3 % 2 == 0 and num4 % 2 != 0) and number1int == number2int:
                    is_combination_valid = True
                    counter +=1
if counter <=6:
    if is_combination_valid and number1int != number2int:
        print(f'{number1int} - {number2int}')
    elif number1int == number2int:
        print("Cannot change the same player.")







