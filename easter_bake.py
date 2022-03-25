import math
import sys

number_of_sugar_breads = int(input())
max_flour = -sys.maxsize
max_sugar = -sys.maxsize
total_used_sugar = 0
total_used_flour = 0
for i in range (number_of_sugar_breads):
    used_sugar = int(input())
    used_flour = int(input())
    total_used_flour += used_flour
    total_used_sugar += used_sugar
    if used_flour > max_flour:
        max_flour = used_flour
    if used_sugar > max_sugar:
        max_sugar = used_sugar
packets_sugar = math.ceil(total_used_sugar / 950)
packets_flour = math.ceil(total_used_flour / 750)

print(f"Sugar: {packets_sugar}")
print(f"Flour: {packets_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
