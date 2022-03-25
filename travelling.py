accumulated_amount = 0
saved_amount_enough = False
command = input()

while command != 'End':
    min_budget = float(input())
    while accumulated_amount < min_budget:
        saved_amount = float(input())
        accumulated_amount += saved_amount
        if accumulated_amount >= min_budget:
            saved_amount_enough = True
            print(f'Going to {command}!')
            break
    accumulated_amount = 0
    command = input()
