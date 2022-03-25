lenght_cm = int(input())
width_cm = int(input())
hight_cm = int(input())
percent_cm = float(input())
volume_aquarium_cm = lenght_cm * width_cm * hight_cm
volume_aquarium_litres = volume_aquarium_cm * 0.001
taken_space = percent_cm / 100
litres_needed = volume_aquarium_litres * (1 - taken_space)
print(litres_needed)