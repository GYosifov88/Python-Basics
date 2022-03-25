number_of_sold_games = int(input())
number_of_hearthstone = 0
number_of_fornite = 0
number_of_overwatch = 0
number_of_others = 0
for i in range (number_of_sold_games):
    game_name = input()
    if game_name == 'Hearthstone':
        number_of_hearthstone += 1
    elif game_name == 'Fornite':
        number_of_fornite += 1
    elif game_name == 'Overwatch':
        number_of_overwatch += 1
    elif game_name != 'Hearthstone' or game_name != 'Fornite' or game_name != 'Overwatch':
        number_of_others += 1

percent_sold_hearthstone = number_of_hearthstone / number_of_sold_games * 100
percent_sold_fornite = number_of_fornite / number_of_sold_games * 100
percent_sold_overwatch = number_of_overwatch / number_of_sold_games * 100
percent_sold_others = number_of_others / number_of_sold_games * 100

print (f'Hearthstone - {percent_sold_hearthstone:.2f}%')
print (f'Fornite - {percent_sold_fornite:.2f}%')
print (f'Overwatch - {percent_sold_overwatch:.2f}%')
print (f'Others - {percent_sold_others:.2f}%')