eggs_size = input()
eggs_color = input()
number_of_packs = int(input())
price_per_egg_pack = 0

if eggs_size == 'Large':
    if eggs_color == 'Red':
        price_per_egg_pack = 16
    elif eggs_color == 'Green':
        price_per_egg_pack = 12
    elif eggs_color == 'Yellow':
        price_per_egg_pack = 9
elif eggs_size == 'Medium':
    if eggs_color == 'Red':
        price_per_egg_pack = 13
    elif eggs_color == 'Green':
        price_per_egg_pack = 9
    elif eggs_color == 'Yellow':
        price_per_egg_pack = 7
elif eggs_size == 'Small':
    if eggs_color == 'Red':
        price_per_egg_pack = 9
    elif eggs_color == 'Green':
        price_per_egg_pack = 8
    elif eggs_color == 'Yellow':
        price_per_egg_pack = 5

income = price_per_egg_pack * number_of_packs
final_income = income - (income * 0.35)

print(f"{final_income:.2f} leva.")