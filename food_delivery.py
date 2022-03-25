chicken_menus = int(input())
fish_menus = int(input())
vegeterian_menus = int(input())
delivery_price = 2.50
price_chicken_menus = chicken_menus * 10.35
price_fish_menus = fish_menus * 12.40
price_vegeterian_menus = vegeterian_menus * 8.15
deserts = 0.20 * (price_vegeterian_menus + price_fish_menus + price_chicken_menus)
total_amount = price_chicken_menus + price_fish_menus + price_vegeterian_menus + deserts + delivery_price
print(total_amount)