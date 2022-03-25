number1 = int(input())
number2 = int(input())

for position in range (number1 , number2 +1):
    odd_sum = 0
    even_sum = 0
    current_position_as_string = str(position)
    for index, digit in enumerate (current_position_as_string):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print (current_position_as_string, end = " ")
