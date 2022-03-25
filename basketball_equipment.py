basketball_year_fee = int(input())
basketball_shoes = basketball_year_fee - (0.40 * basketball_year_fee)
basketball_dress = basketball_shoes - (0.20 * basketball_shoes)
basketball_ball = basketball_dress * 1 / 4
basketball_accessoaries = basketball_ball * 1 / 5
total_amount = basketball_year_fee + basketball_shoes + basketball_dress + basketball_ball + basketball_accessoaries
print(total_amount)