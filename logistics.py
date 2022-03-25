number_of_cargos = int(input())
total_tons = 0
bus_tons = 0
truck_tons = 0
train_tons = 0

for i in range (number_of_cargos):
    cargo_tons = int(input())
    if cargo_tons <= 3:
        bus_tons += cargo_tons
        total_tons += cargo_tons
    elif 4 <= cargo_tons <= 11:
        truck_tons += cargo_tons
        total_tons += cargo_tons
    elif cargo_tons >= 12:
        train_tons += cargo_tons
        total_tons += cargo_tons

bus_price = bus_tons * 200
truck_price = truck_tons * 175
train_price = train_tons * 120
total_price = bus_price + train_price + truck_price
average_price = total_price / total_tons
bus_percent = bus_tons / total_tons * 100
truck_percent = truck_tons / total_tons * 100
train_percent = train_tons / total_tons * 100

print (f'{average_price:.2f}')
print (f'{bus_percent:.2f}%')
print (f'{truck_percent:.2f}%')
print (f'{train_percent:.2f}%')