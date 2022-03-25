import sys

number_of_sugar_breads = int(input())
best_chef = ''
max_grade = -sys.maxsize
for i in range (number_of_sugar_breads):
    chef_name = input()
    total_grade = 0
    while True:
        grade = input()

        if grade == "Stop":
            print(f"{chef_name} has {total_grade} points.")
            if total_grade == max_grade:
                print(f"{chef_name} is the new number 1!")
            break

        total_grade += int(grade)

        if total_grade >= max_grade:
            max_grade = total_grade
            best_chef = chef_name

print(f"{best_chef} won competition with {max_grade} points!")
