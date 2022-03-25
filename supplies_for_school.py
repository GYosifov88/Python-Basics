packages_pen = int(input())
packages_markers = int(input())
litres_cleaning = int(input())
discount = int(input())
price_pen = packages_pen * 5.80
price_markers = packages_markers * 7.20
price_litres_cleaning = litres_cleaning * 1.20
total_amount = (price_markers + price_pen + price_litres_cleaning)
amount_with_discount = total_amount - (total_amount * discount / 100)
print(amount_with_discount)