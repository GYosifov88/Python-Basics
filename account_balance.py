total = 0
funds = 0
while True:
    funds = input()
    if funds == 'NoMoreMoney':
        break
    elif float(funds) < 0:
        print('Invalid operation!')
        break
    print(f"Increase: {float(funds):.2f}")
    total += float(funds)


print(f'Total: {float(total):.2f}')