import math
number_of_paint_boxes = int(input())
number_of_rolls = int(input())
price_per_gloves = float(input())
price_per_brush = float(input())

number_of_gloves = math.ceil(number_of_rolls * 35 / 100)
number_of_brushes = math.floor(number_of_paint_boxes * 48 / 100)

cost_of_paint_boxes = number_of_paint_boxes * 21.50
cost_of_rolls = number_of_rolls * 5.20
cost_of_gloves = number_of_gloves * price_per_gloves
cost_of_brushes = number_of_brushes * price_per_brush
total_cost = cost_of_brushes + cost_of_gloves + cost_of_rolls + cost_of_paint_boxes

delivery_cost = total_cost / 15

print (f"This delivery will cost {delivery_cost:.2f} lv." )