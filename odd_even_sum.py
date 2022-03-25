num = int(input())
odd_sum = 0
even_sum = 0
for i in range (num):
    current_num = int(input())

    if i % 2 == 0:
        even_sum +=current_num
    else:
        odd_sum +=current_num

    diff = abs(even_sum - odd_sum)

if even_sum == odd_sum:
    print ('Yes')
    print (f'Sum = {even_sum}')
else:
    print ('No')
    print (f'Diff = {diff}')
