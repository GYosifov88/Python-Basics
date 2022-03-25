stadium_capacity = int(input())
number_of_fans = int(input())
sectorA = 0
sectorB = 0
sectorV = 0
sectorG = 0
team1_fan = 0
team2_fan = 0
for fans in range (number_of_fans):
    sector = input()
    if sector == 'A':
        sectorA +=1
        team1_fan +=1
    elif sector == 'B':
        sectorB += 1
        team1_fan += 1
    elif sector == 'V':
        sectorV += 1
        team2_fan += 1
    elif sector == 'G':
        sectorG += 1
        team2_fan += 1

percent_sector_a = sectorA / number_of_fans * 100
percent_sector_b = sectorB / number_of_fans * 100
percent_sector_v = sectorV / number_of_fans * 100
percent_sector_g = sectorG / number_of_fans * 100
percent_team_one = team1_fan / stadium_capacity * 100
percent_team_two = team2_fan / stadium_capacity * 100
percent_of_both_teams = percent_team_one + percent_team_two

print (f'{percent_sector_a:.2f}%')
print (f'{percent_sector_b:.2f}%')
print (f'{percent_sector_v:.2f}%')
print (f'{percent_sector_g:.2f}%')
print (f'{percent_of_both_teams:.2f}%')

