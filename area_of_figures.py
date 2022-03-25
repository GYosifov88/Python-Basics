from math import pi
from math import floor

type =str(input())

if type == 'square':
 side_a_lenght = float(input())
 area = round(side_a_lenght * side_a_lenght, 3)
 print(f"{area:.3f}")
elif type == 'rectangle':
 side_a = float(input())
 side_b = float(input())
 area = round(side_a * side_b, 3)
 print(f"{area:.3f}")
elif type == 'circle':
 radius = float(input())
 area = round(radius * radius * pi, 3)
 print(f"{area:.3f}")
elif type == 'triangle':
 side_a = float(input())
 hight = float(input())
 area = round((side_a * hight) / 2, 3)
 print(f"{area:.3f}")