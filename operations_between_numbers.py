number1 = int(input())
number2 = int(input())
operator = input()
result = 0
if operator == '+':
    result = number1 + number2
    even_or_odd = result % 2
    if even_or_odd == 0:
       print (f'{number1} + {number2} = {result} - even')
    elif even_or_odd !=0:
        print(f'{number1} + {number2} = {result} - odd')
elif operator == '-':
    result = number1 - number2
    even_or_odd = result % 2
    if even_or_odd == 0:
       print (f'{number1} - {number2} = {result} - even')
    elif even_or_odd !=0:
        print(f'{number1} - {number2} = {result} - odd')
elif operator == '*':
    result = number1 * number2
    even_or_odd = result % 2
    if even_or_odd == 0:
       print (f'{number1} * {number2} = {result} - even')
    elif even_or_odd !=0:
        print(f'{number1} * {number2} = {result} - odd')
elif operator == '/' and number2 !=0:
    result = number1 / number2
    print(f'{number1} / {number2} = {result:.2f}')
elif operator == '%' and number2 !=0:
    result = number1 % number2
    print(f'{number1} % {number2} = {result}')
elif (operator == '/' or operator == '%') and number2 == 0:
    print(f'Cannot divide {number1} by zero')