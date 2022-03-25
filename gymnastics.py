country = input()
game = input()
max_points = 20
if country == 'Russia':
    if game == 'ribbon':
        performance = 9.100
        severity = 9.400
        total_points = performance + severity
    elif game == 'hoop':
        performance = 9.300
        severity = 9.800
        total_points = performance + severity
    elif game == 'rope':
        performance = 9.600
        severity = 9.000
        total_points = performance + severity
elif country == 'Bulgaria':
    if game == 'ribbon':
        performance = 9.600
        severity = 9.400
        total_points = performance + severity
    elif game == 'hoop':
        performance = 9.550
        severity = 9.750
        total_points = performance + severity
    elif game == 'rope':
        performance = 9.500
        severity = 9.400
        total_points = performance + severity
elif country == 'Italy':
    if game == 'ribbon':
        performance = 9.200
        severity = 9.500
        total_points = performance + severity
    elif game == 'hoop':
        performance = 9.450
        severity = 9.350
        total_points = performance + severity
    elif game == 'rope':
        performance = 9.700
        severity = 9.150
        total_points = performance + severity

points_remained = max_points - total_points
percent_remained = points_remained / 20 * 100

print(f"The team of {country} get {total_points:.3f} on {game}.")
print(f"{percent_remained:.2f}%")

