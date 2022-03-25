bitcoins = int(input())
chinese_juan = float(input())
commision = float(input())

price_bitcoin_leva= bitcoins * 1168
price_chinese_juan_dolars = chinese_juan * 0.15
price_chinese_juan_leva = price_chinese_juan_dolars * 1.76
total_leva = price_bitcoin_leva + price_chinese_juan_leva

full_amount_euro = total_leva / 1.95
commision_amount = full_amount_euro * commision / 100

total_amount_euro = full_amount_euro - commision_amount

print(f'{total_amount_euro:.2f}')