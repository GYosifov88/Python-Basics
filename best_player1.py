import sys


top_player = ''
top_scorer = -sys.maxsize
player_name = input()
while player_name != 'END':
    goals = int(input())
    if goals > top_scorer:
        top_player = player_name
        top_scorer = goals

    if goals >= 10:
        top_player = player_name
        top_scorer = goals
        break
    # top_scorer = goals
    # top_player = player_name

    player_name = input()
print (f'{top_player} is the best player!')
if top_scorer >= 3:

    print (f'He has scored {goals} goals and made a hat-trick !!!')
else:
    # print (f'{top_player} is the best player!')
    print (f'He has scored {top_scorer} goals.')






