import sys

max_num = -sys.maxsize

while True:
    num = input()
    if num == 'Stop':
        break
    elif int(num) > max_num:
        max_num = int(num)
print(max_num)