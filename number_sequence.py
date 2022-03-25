import sys

num = int(input())

max_num = -sys.maxsize
min_num = sys.maxsize

for _ in range (num):
 x = int(input())
 if x > max_num:
    max_num = x
 if x < min_num:
    min_num = x

print (f'Max number: {max_num}')
print (f'Min number: {min_num}')