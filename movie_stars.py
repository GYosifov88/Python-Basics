budget_for_actors = float(input())
budget_left = budget_for_actors
actor_name = input()
salary = 0
while actor_name != 'ACTION':

    if len(actor_name) <= 15:
        salary = float(input())
        if salary > budget_left:
            budget_left = budget_left - salary
            break
        else:
            budget_left = budget_left - salary
    elif len(actor_name) > 15:
        salary = budget_left * 20 / 100
        if salary > budget_left:
            budget_left = budget_left - salary
            break
        else:
            budget_left = budget_left - salary



    actor_name = input()

difference = abs(budget_left)

if budget_left < salary or budget_left < 0:
    print (f'We need {difference:.2f} leva for our actors.')
elif budget_left > 0:
    print (f'We are left with {difference:.2f} leva.')