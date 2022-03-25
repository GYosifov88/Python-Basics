city_name = input()
package_name = input()
vip_discount = input()
days = int(input())
price_per_day = 0
total_cost = 0
vip_discount_percent = 0
if city_name == 'Bansko' or city_name == 'Borovets':
    if package_name == 'withEquipment':
        price_per_day = 100
        vip_discount_percent = 10
    elif package_name == 'noEquipment':
        price_per_day = 80
        vip_discount_percent = 5
elif city_name == 'Varna' or city_name == 'Burgas':
    if package_name == 'withBreakfast':
        price_per_day = 130
        vip_discount_percent = 12
    elif package_name == 'noBreakfast':
        price_per_day = 100
        vip_discount_percent = 7

total_cost = price_per_day * days

if days >= 7:
    total_cost = price_per_day * (days - 1)

if vip_discount == 'yes':
    total_cost = total_cost - (total_cost * vip_discount_percent / 100)
elif vip_discount == 'no':
    total_cost = total_cost


if days < 1:
    print('Days must be positive number!')

if days >= 1 and (city_name == "Bansko" or city_name == 'Borovets' or city_name == 'Varna' or city_name == 'Burgas') and (package_name == 'withEquipment' or package_name == 'noEquipment' or package_name == 'withBreakfast' or package_name == 'noBreakfast'):
    print(f'The price is {total_cost:.2f}lv! Have a nice time!')

elif days >= 1 and (city_name != "Bansko" or city_name != 'Borovets' or city_name != 'Varna' or city_name != 'Burgas'):
    print ('Invalid input!')

elif days >= 1 and (package_name!= 'withEquipment' or package_name!= 'noEquipment' or package_name!= 'withBreakfast' or package_name!= 'noBreakfast'):
    print('Invalid input!')