import sys

n = int(input())
max_num = -sys.maxsize
total = 0

for i in range (0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    total += num

if max_num == total - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = abs(max_num - (total - max_num))
    print ('No')
    print (f'Diff = {diff}')