starting_num = int(input())
finishing_num = int(input())
magic_num = int(input())
combination_counter = 0
total_combination = False
for i in range (starting_num, finishing_num + 1):
    for j in range (starting_num, finishing_num +1):
        combination_counter += 1
        if i + j == magic_num:
            total_combination = True
            print(f'Combination N:{combination_counter} ({i} + {j} = {magic_num})')
            break
    if total_combination:
        break

if not total_combination:
    print(f'{combination_counter} combinations - neither equals {magic_num}')
