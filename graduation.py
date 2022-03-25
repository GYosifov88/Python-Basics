student_name = input()
bad_grade = 0
year = 1
total = 0
while True:
    if bad_grade > 1:
        print (f'{student_name} has been excluded at {year} grade')
        break
    grade = float(input())

    if grade >= 4:
        total += grade
        if year == 12:
            average_grade = total / 12
            print (f'"{student_name} graduated. Average grade: {average_grade:.2f}"')
            break
        year +=1
    elif grade < 4:
        bad_grade +=1