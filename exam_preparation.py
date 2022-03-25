bad_grades = int(input())
number_of_problems = 0
last_problem = ''
number_of_bad_grades = 0
grade = 0
is_expelled = False
total_grade = 0
problem = input()
while problem != 'Enough':
    grade = int(input())
    total_grade += grade
    if grade <= 4:
        number_of_bad_grades += 1
        if number_of_bad_grades == bad_grades:
            is_expelled = True
            break

    last_problem = problem

    number_of_problems += 1
    problem = input()

if is_expelled:
    print(f'You need a break, {number_of_bad_grades} poor grades.')
else:
    average_grade = total_grade / number_of_problems
    print(f'Average score: {average_grade:.2f}')
    print (f'Number of problems: {number_of_problems}')
    print (f'Last problem: {last_problem}')
